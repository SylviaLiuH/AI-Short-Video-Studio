from tts_service import generate_audio, get_audio_duration


def main():
    text = "镜子里的世界，好像正在呼唤我。"

    audio_path = generate_audio(
        text=text,
        scene_number=1,
    )

    duration = get_audio_duration(
        audio_path
    )

    print("TTS 生成成功！")
    print("保存路径：", audio_path)
    print(
        "音频时长：",
        round(duration, 2),
        "秒",
    )


if __name__ == "__main__":
    main()