from tts_service import generate_scene_audio, generate_srt


def main():
    scenes = [
        {
            "scene_number": 1,
            "voiceover": "镜子里的世界，好像正在呼唤我。",
        },
        {
            "scene_number": 2,
            "voiceover": "我慢慢靠近，镜面突然泛起了蓝色的光。",
        },
        {
            "scene_number": 3,
            "voiceover": "下一秒，我竟然穿过了镜子。",
        },
        {
            "scene_number": 4,
            "voiceover": "镜子后面，是一个完全不同的世界。",
        },
        {
            "scene_number": 5,
            "voiceover": "那里的一切既陌生，又好像在哪里见过。",
        },
        {
            "scene_number": 6,
            "voiceover": "而真正让我害怕的是，镜子另一边也有一个我。",
        },
    ]

    audio_results = []

    for scene in scenes:
        print(
            f"正在生成镜头 {scene['scene_number']} 配音..."
        )

        result = generate_scene_audio(
            scene
        )

        audio_results.append(
            result
        )

        print(
            f"镜头 {scene['scene_number']} 完成，"
            f"时长 {result['duration']:.2f} 秒"
        )

    srt_path = generate_srt(
        audio_results
    )

    print()
    print("全部 TTS 生成成功！")
    print("字幕生成成功！")
    print("SRT 路径：", srt_path)


if __name__ == "__main__":
    main()