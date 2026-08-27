from pathlib import Path

from tts_service import get_audio_duration
from video_service import generate_final_video


IMAGES_DIR = Path("outputs/images")
AUDIO_DIR = Path("outputs/audio")
SUBTITLE_PATH = Path("outputs/subtitles/video.srt")


def find_latest_scene_image(scene_number: int) -> str:
    """
    找到某个镜头最新生成的图片。
    """

    image_files = list(
        IMAGES_DIR.glob(
            f"scene_{scene_number}_*.png"
        )
    )

    if not image_files:
        raise FileNotFoundError(
            f"没有找到镜头 {scene_number} 的图片。"
        )

    latest_image = max(
        image_files,
        key=lambda path: path.stat().st_mtime,
    )

    return str(latest_image)


def main():
    scene_images = {}
    scene_audio = {}

    for scene_number in range(1, 7):

        # -------------------------
        # 图片
        # -------------------------
        image_path = find_latest_scene_image(
            scene_number
        )

        scene_images[
            str(scene_number)
        ] = image_path

        # -------------------------
        # 音频
        # -------------------------
        audio_path = (
            AUDIO_DIR
            / f"scene_{scene_number}.mp3"
        )

        if not audio_path.exists():
            raise FileNotFoundError(
                f"没有找到镜头 {scene_number} 的音频："
                f"{audio_path}"
            )

        duration = get_audio_duration(
            str(audio_path)
        )

        scene_audio[
            str(scene_number)
        ] = {
            "scene_number": scene_number,
            "audio_path": str(audio_path),
            "duration": duration,
        }

        print(
            f"镜头 {scene_number}："
            f"图片 ✓  音频 ✓  "
            f"{duration:.2f} 秒"
        )

    # -------------------------
    # 字幕
    # -------------------------
    if not SUBTITLE_PATH.exists():
        raise FileNotFoundError(
            f"没有找到字幕文件："
            f"{SUBTITLE_PATH}"
        )

    print()
    print("素材检查完成！")
    print("开始调用 FFmpeg 合成视频...")
    print()

    final_video_path = generate_final_video(
        scene_images=scene_images,
        scene_audio=scene_audio,
        subtitle_path=str(
            SUBTITLE_PATH
        ),
    )

    print()
    print("🎉 视频生成成功！")
    print(
        "保存路径：",
        final_video_path,
    )


if __name__ == "__main__":
    main()