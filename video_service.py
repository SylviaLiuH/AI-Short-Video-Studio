import shutil
import subprocess
from datetime import datetime
from pathlib import Path


OUTPUT_DIR = Path("outputs/videos")
TEMP_DIR = OUTPUT_DIR / "_temp"

VIDEO_WIDTH = 720
VIDEO_HEIGHT = 1280
VIDEO_FPS = 30


def _run_ffmpeg(command: list[str]) -> None:
    """
    执行 FFmpeg 命令。

    如果失败，则抛出包含 FFmpeg 错误信息的异常。
    """

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    if result.returncode != 0:
        raise RuntimeError(
            "FFmpeg 执行失败。\n\n"
            f"命令：\n{' '.join(command)}\n\n"
            f"错误信息：\n{result.stderr}"
        )


def check_ffmpeg() -> bool:
    """
    检查 FFmpeg 是否可以正常调用。
    """

    try:
        result = subprocess.run(
            [
                "ffmpeg",
                "-version",
            ],
            capture_output=True,
            text=True,
        )

        return result.returncode == 0

    except FileNotFoundError:
        return False


def _prepare_temp_dir() -> None:
    """
    清理并创建视频临时目录。
    """

    if TEMP_DIR.exists():
        shutil.rmtree(
            TEMP_DIR
        )

    TEMP_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )


def _create_scene_clip(
    image_path: str,
    audio_path: str,
    duration: float,
    scene_number: int,
) -> str:
    """
    将单张图片和对应 MP3 合成为一个 Scene MP4。
    """

    image_file = Path(
        image_path
    )

    audio_file = Path(
        audio_path
    )

    if not image_file.exists():
        raise FileNotFoundError(
            f"镜头 {scene_number} 图片不存在："
            f"{image_file}"
        )

    if not audio_file.exists():
        raise FileNotFoundError(
            f"镜头 {scene_number} 音频不存在："
            f"{audio_file}"
        )

    output_path = (
        TEMP_DIR
        / f"scene_{scene_number}.mp4"
    )

    video_filter = (
        f"scale="
        f"{VIDEO_WIDTH}:"
        f"{VIDEO_HEIGHT}:"
        f"force_original_aspect_ratio=decrease,"
        f"pad="
        f"{VIDEO_WIDTH}:"
        f"{VIDEO_HEIGHT}:"
        f"(ow-iw)/2:"
        f"(oh-ih)/2:"
        f"black,"
        f"setsar=1"
    )

    command = [
        "ffmpeg",
        "-y",

        # 图片循环
        "-loop",
        "1",

        # 图片输入
        "-i",
        str(image_file),

        # 音频输入
        "-i",
        str(audio_file),

        # 视频滤镜
        "-vf",
        video_filter,

        # 精确控制 Scene 时长
        "-t",
        f"{duration:.3f}",

        # 帧率
        "-r",
        str(VIDEO_FPS),

        # 视频编码
        "-c:v",
        "libx264",

        # 编码速度
        "-preset",
        "medium",

        # 视频质量
        "-crf",
        "20",

        # 音频编码
        "-c:a",
        "aac",

        "-b:a",
        "192k",

        # 兼容播放器
        "-pix_fmt",
        "yuv420p",

        "-movflags",
        "+faststart",

        "-shortest",

        str(output_path),
    ]

    _run_ffmpeg(
        command
    )

    return str(
        output_path
    )


def _create_concat_file(
    scene_clips: list[str],
) -> Path:
    """
    创建 FFmpeg concat 文件列表。
    """

    concat_path = (
        TEMP_DIR
        / "concat.txt"
    )

    lines = []

    for clip in scene_clips:
        absolute_path = (
            Path(clip)
            .resolve()
            .as_posix()
        )

        # 防止路径中的单引号影响 concat 文件
        absolute_path = (
            absolute_path.replace(
                "'",
                "'\\''",
            )
        )

        lines.append(
            f"file '{absolute_path}'"
        )

    concat_path.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    return concat_path


def _concat_scene_clips(
    scene_clips: list[str],
) -> str:
    """
    将所有 Scene MP4 顺序拼接。
    """

    concat_file = (
        _create_concat_file(
            scene_clips
        )
    )

    output_path = (
        TEMP_DIR
        / "video_without_subtitles.mp4"
    )

    command = [
        "ffmpeg",
        "-y",

        "-f",
        "concat",

        "-safe",
        "0",

        "-i",
        str(concat_file),

        # Scene 参数完全一致，
        # 因此可以直接 Copy
        "-c",
        "copy",

        str(output_path),
    ]

    _run_ffmpeg(
        command
    )

    return str(
        output_path
    )


def _escape_subtitle_path(
    subtitle_path: Path,
) -> str:
    """
    将 Windows 路径转换成 FFmpeg subtitles filter
    可以识别的格式。
    """

    path = (
        subtitle_path
        .resolve()
        .as_posix()
    )

    # Windows C:/xxx
    # 在 FFmpeg filter 中需要转义 :
    path = path.replace(
        ":",
        "\\:",
    )

    path = path.replace(
        "'",
        "\\'",
    )

    return path


def _burn_subtitles(
    input_video: str,
    subtitle_path: str,
    output_video: str,
) -> str:
    """
    将 SRT 字幕烧录到视频中。
    """

    subtitle_file = Path(
        subtitle_path
    )

    if not subtitle_file.exists():
        raise FileNotFoundError(
            f"SRT 字幕不存在："
            f"{subtitle_file}"
        )

    subtitle_filter_path = (
        _escape_subtitle_path(
            subtitle_file
        )
    )

    subtitle_filter = (
        f"subtitles="
        f"'{subtitle_filter_path}'"
        f":force_style="
        f"'FontName=Microsoft YaHei,"
        f"FontSize=22,"
        f"PrimaryColour=&H00FFFFFF,"
        f"OutlineColour=&H00000000,"
        f"BorderStyle=1,"
        f"Outline=2,"
        f"Shadow=0,"
        f"Alignment=2,"
        f"MarginV=80'"
    )

    command = [
        "ffmpeg",
        "-y",

        "-i",
        input_video,

        "-vf",
        subtitle_filter,

        "-c:v",
        "libx264",

        "-preset",
        "medium",

        "-crf",
        "20",

        "-c:a",
        "copy",

        "-pix_fmt",
        "yuv420p",

        "-movflags",
        "+faststart",

        output_video,
    ]

    _run_ffmpeg(
        command
    )

    return output_video


def generate_final_video(
    scene_images: dict,
    scene_audio: dict,
    subtitle_path: str,
) -> str:
    """
    根据：

    - Scene Images
    - Scene Audio
    - SRT Subtitle

    生成最终 MP4。

    返回最终视频路径。
    """

    if not check_ffmpeg():
        raise RuntimeError(
            "FFmpeg 无法使用，"
            "请确认 FFmpeg 已安装并加入 PATH。"
        )

    if not scene_images:
        raise ValueError(
            "没有找到任何分镜图片。"
        )

    if not scene_audio:
        raise ValueError(
            "没有找到任何分镜配音。"
        )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    _prepare_temp_dir()

    # 按 Scene Number 排序
    scene_numbers = sorted(
        scene_audio.keys(),
        key=lambda value: int(value),
    )

    scene_clips = []

    for scene_number_text in scene_numbers:

        scene_number = int(
            scene_number_text
        )

        image_path = (
            scene_images.get(
                scene_number_text
            )
        )

        audio_info = (
            scene_audio.get(
                scene_number_text
            )
        )

        if not image_path:
            raise ValueError(
                f"缺少镜头 "
                f"{scene_number} 图片。"
            )

        if not audio_info:
            raise ValueError(
                f"缺少镜头 "
                f"{scene_number} 配音。"
            )

        audio_path = (
            audio_info.get(
                "audio_path"
            )
        )

        duration = (
            audio_info.get(
                "duration"
            )
        )

        if not audio_path:
            raise ValueError(
                f"镜头 "
                f"{scene_number} "
                f"缺少 audio_path。"
            )

        if not duration:
            raise ValueError(
                f"镜头 "
                f"{scene_number} "
                f"缺少音频时长。"
            )

        clip_path = (
            _create_scene_clip(
                image_path=image_path,
                audio_path=audio_path,
                duration=float(
                    duration
                ),
                scene_number=scene_number,
            )
        )

        scene_clips.append(
            clip_path
        )

    # 拼接六个 Scene
    video_without_subtitles = (
        _concat_scene_clips(
            scene_clips
        )
    )

    timestamp = (
        datetime.now()
        .strftime(
            "%Y%m%d_%H%M%S"
        )
    )

    final_video_path = (
        OUTPUT_DIR
        / f"final_video_{timestamp}.mp4"
    )

    # 烧录 SRT
    _burn_subtitles(
        input_video=(
            video_without_subtitles
        ),
        subtitle_path=(
            subtitle_path
        ),
        output_video=str(
            final_video_path
        ),
    )

    return str(
        final_video_path
    )