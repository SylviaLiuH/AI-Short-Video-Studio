import asyncio
from pathlib import Path

import edge_tts
from mutagen.mp3 import MP3


OUTPUT_DIR = Path("outputs/audio")

DEFAULT_VOICE = "zh-CN-XiaoxiaoNeural"
DEFAULT_RATE = "+0%"
DEFAULT_VOLUME = "+0%"


async def _generate_audio_async(
    text: str,
    output_path: Path,
    voice: str = DEFAULT_VOICE,
    rate: str = DEFAULT_RATE,
    volume: str = DEFAULT_VOLUME,
):
    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=rate,
        volume=volume,
    )

    await communicate.save(
        str(output_path)
    )


def generate_audio(
    text: str,
    scene_number: int,
    voice: str = DEFAULT_VOICE,
) -> str:
    """
    将单个分镜旁白生成 MP3。
    """

    if not text or not text.strip():
        raise ValueError("旁白文本不能为空。")

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path = (
        OUTPUT_DIR
        / f"scene_{scene_number}.mp3"
    )

    asyncio.run(
        _generate_audio_async(
            text=text,
            output_path=output_path,
            voice=voice,
        )
    )

    return str(output_path)


def get_audio_duration(
    audio_path: str,
) -> float:
    """
    获取 MP3 音频时长，单位：秒。
    """

    audio = MP3(audio_path)

    return float(
        audio.info.length
    )


def generate_scene_audio(
    scene: dict,
) -> dict:
    """
    为一个 Scene 生成语音并返回相关信息。
    """

    scene_number = scene.get(
        "scene_number",
        1,
    )

    voiceover = scene.get(
        "voiceover",
        "",
    )

    audio_path = generate_audio(
        text=voiceover,
        scene_number=scene_number,
    )

    duration = get_audio_duration(
        audio_path
    )

    return {
        "scene_number": scene_number,
        "voiceover": voiceover,
        "audio_path": audio_path,
        "duration": duration,
    }


def _format_srt_time(
    seconds: float,
) -> str:
    """
    将秒转换成 SRT 时间格式：
    00:00:00,000
    """

    milliseconds = int(
        seconds * 1000
    )

    hours = (
        milliseconds // 3_600_000
    )

    milliseconds %= 3_600_000

    minutes = (
        milliseconds // 60_000
    )

    milliseconds %= 60_000

    secs = (
        milliseconds // 1000
    )

    millis = (
        milliseconds % 1000
    )

    return (
        f"{hours:02}:"
        f"{minutes:02}:"
        f"{secs:02},"
        f"{millis:03}"
    )


def generate_srt(
    audio_results: list[dict],
    output_path: str = "outputs/subtitles/video.srt",
) -> str:
    """
    根据每个分镜音频的真实时长生成 SRT 字幕。
    """

    srt_path = Path(
        output_path
    )

    srt_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    current_time = 0.0

    lines = []

    for index, item in enumerate(
        audio_results,
        start=1,
    ):
        duration = item[
            "duration"
        ]

        text = item[
            "voiceover"
        ]

        start_time = current_time
        end_time = (
            current_time + duration
        )

        lines.append(
            str(index)
        )

        lines.append(
            f"{_format_srt_time(start_time)} "
            f"--> "
            f"{_format_srt_time(end_time)}"
        )

        lines.append(
            text
        )

        lines.append("")

        current_time = end_time

    srt_path.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    return str(srt_path)