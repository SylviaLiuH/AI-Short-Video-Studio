import json
from pathlib import Path

import streamlit as st

from ollama_service import generate_video_plan


# =========================
# 页面配置
# =========================
st.set_page_config(
    page_title="AI Short Video Studio",
    page_icon="🎬",
    layout="wide",
)


# =========================
# Session State
# =========================
if "video_plan" not in st.session_state:
    st.session_state.video_plan = None

if "video_meta" not in st.session_state:
    st.session_state.video_meta = None

if "scene_images" not in st.session_state:
    st.session_state.scene_images = {}

if "scene_audio" not in st.session_state:
    st.session_state.scene_audio = {}

if "subtitle_path" not in st.session_state:
    st.session_state.subtitle_path = None


# =========================
# Lazy Load：图片生成
# =========================
def generate_scene_image_lazy(scene: dict) -> str:
    """
    点击生成图片后再导入 Stable Diffusion，
    避免 Streamlit 启动时立即加载重模型。
    """
    from image_service import generate_scene_image

    return generate_scene_image(scene)


# =========================
# Lazy Load：TTS
# =========================
def generate_scene_audio_lazy(scene: dict) -> dict:
    """
    点击生成配音后再导入 TTS 模块。
    """
    from tts_service import generate_scene_audio

    return generate_scene_audio(scene)


def generate_srt_lazy(
    audio_results: list[dict],
) -> str:
    """
    根据音频真实时长生成 SRT 字幕。
    """
    from tts_service import generate_srt

    return generate_srt(audio_results)


# =========================
# 导出函数
# =========================
def build_script_text(result: dict) -> str:
    return f"""AI Short Video Studio

标题：
{result.get("title", "")}

前 3 秒 Hook：
{result.get("hook", "")}

完整脚本：
{result.get("script", "")}
"""


def build_storyboard_markdown(result: dict) -> str:
    lines = [
        "# AI Short Video Storyboard",
        "",
        "## 标题",
        result.get("title", ""),
        "",
        "## Hook",
        result.get("hook", ""),
        "",
        "## 完整脚本",
        result.get("script", ""),
        "",
        "## 分镜",
        "",
    ]

    for scene in result.get("scenes", []):
        scene_number = scene.get(
            "scene_number",
            "",
        )

        lines.extend(
            [
                f"### 镜头 {scene_number}",
                "",
                "**画面**",
                "",
                scene.get("visual", ""),
                "",
                "**旁白**",
                "",
                scene.get("voiceover", ""),
                "",
                "**音效 / BGM**",
                "",
                scene.get("sound", ""),
                "",
                "**Image Prompt**",
                "",
                scene.get("image_prompt", ""),
                "",
                "**Video Prompt**",
                "",
                scene.get("video_prompt", ""),
                "",
                "---",
                "",
            ]
        )

    return "\n".join(lines)


# =========================
# 页面标题
# =========================
st.title("🎬 AI Short Video Studio")

st.caption(
    "把一个简单创意，快速变成结构化短视频方案、"
    "AI 视觉素材、配音与字幕。"
)


# =========================
# 用户输入
# =========================
topic = st.text_area(
    "你想做什么内容？",
    placeholder="例如：一个机器人第一次看到大海",
    height=120,
)

col1, col2 = st.columns(2)

with col1:
    style = st.selectbox(
        "视频风格",
        [
            "悬疑",
            "治愈",
            "搞笑",
            "奇幻",
            "情绪故事",
        ],
    )

with col2:
    duration = st.selectbox(
        "视频时长",
        [
            "30 秒",
            "45 秒",
            "60 秒",
        ],
    )


# =========================
# 生成视频方案
# =========================
if st.button(
    "✨ 生成视频方案",
    type="primary",
    use_container_width=True,
):
    if not topic.strip():
        st.warning("先输入一个主题～")

    else:
        try:
            with st.spinner(
                "AI 正在生成短视频方案和视觉 Prompt..."
            ):
                result = generate_video_plan(
                    topic=topic,
                    style=style,
                    duration=duration,
                )

            st.session_state.video_plan = result

            st.session_state.video_meta = {
                "topic": topic,
                "style": style,
                "duration": duration,
            }

            # 新方案生成后清空旧素材
            st.session_state.scene_images = {}
            st.session_state.scene_audio = {}
            st.session_state.subtitle_path = None

            st.success("生成完成！")

        except Exception as e:
            st.error(
                "生成失败，请检查 Ollama 是否正在运行，"
                "或 AI 返回格式是否正确。"
            )

            with st.expander("查看错误信息"):
                st.code(str(e))


# =========================
# 展示生成结果
# =========================
result = st.session_state.video_plan

if result:

    st.divider()

    # =========================
    # 标题
    # =========================
    st.subheader("🎬 标题")
    st.write(
        result.get(
            "title",
            "",
        )
    )

    # =========================
    # Hook
    # =========================
    st.subheader("⚡ 前 3 秒 Hook")
    st.info(
        result.get(
            "hook",
            "",
        )
    )

    # =========================
    # 脚本
    # =========================
    st.subheader("📝 短视频脚本")
    st.write(
        result.get(
            "script",
            "",
        )
    )

    scenes = result.get(
        "scenes",
        [],
    )

    # =====================================================
    # AI 图片批量生成
    # =====================================================
    st.divider()

    st.subheader("🖼️ AI 分镜图片")

    existing_image_count = 0

    for scene in scenes:
        scene_number = str(
            scene.get(
                "scene_number",
                "",
            )
        )

        image_path = (
            st.session_state.scene_images.get(
                scene_number
            )
        )

        if (
            image_path
            and Path(image_path).exists()
        ):
            existing_image_count += 1

    st.caption(
        f"当前已生成："
        f"{existing_image_count} / {len(scenes)} 张"
    )

    if st.button(
        "🚀 一键生成全部分镜图片",
        type="primary",
        use_container_width=True,
    ):
        if not scenes:
            st.warning(
                "当前没有可生成的分镜。"
            )

        else:
            progress_bar = st.progress(0)

            status_text = st.empty()

            errors = []

            total_scenes = len(
                scenes
            )

            for index, scene in enumerate(
                scenes
            ):
                scene_number = scene.get(
                    "scene_number",
                    index + 1,
                )

                image_key = str(
                    scene_number
                )

                existing_path = (
                    st.session_state.scene_images.get(
                        image_key
                    )
                )

                if (
                    existing_path
                    and Path(
                        existing_path
                    ).exists()
                ):
                    status_text.info(
                        f"镜头 {scene_number} "
                        f"已有图片，跳过。"
                    )

                else:
                    try:
                        status_text.info(
                            f"RTX 3060 正在生成镜头 "
                            f"{scene_number} / "
                            f"{total_scenes}..."
                        )

                        image_path = (
                            generate_scene_image_lazy(
                                scene
                            )
                        )

                        st.session_state.scene_images[
                            image_key
                        ] = image_path

                    except Exception as e:
                        errors.append(
                            (
                                scene_number,
                                str(e),
                            )
                        )

                progress_bar.progress(
                    (index + 1)
                    / total_scenes
                )

            if errors:
                status_text.warning(
                    "批量生成完成，"
                    "但部分镜头失败。"
                )

                with st.expander(
                    "查看批量生成错误"
                ):
                    for (
                        scene_number,
                        error,
                    ) in errors:
                        st.markdown(
                            f"**镜头 "
                            f"{scene_number}**"
                        )
                        st.code(
                            error
                        )

            else:
                status_text.success(
                    "🎉 全部分镜图片生成完成！"
                )


    # =====================================================
    # TTS + Subtitle
    # =====================================================
    st.divider()

    st.subheader("🔊 AI 配音与字幕")

    existing_audio_count = 0

    for scene in scenes:
        scene_number = str(
            scene.get(
                "scene_number",
                "",
            )
        )

        audio_info = (
            st.session_state.scene_audio.get(
                scene_number
            )
        )

        if audio_info:
            audio_path = audio_info.get(
                "audio_path"
            )

            if (
                audio_path
                and Path(
                    audio_path
                ).exists()
            ):
                existing_audio_count += 1

    st.caption(
        f"当前已生成："
        f"{existing_audio_count} / "
        f"{len(scenes)} 段配音"
    )

    if st.button(
        "🔊 一键生成全部配音与字幕",
        type="primary",
        use_container_width=True,
    ):
        if not scenes:
            st.warning(
                "当前没有可生成配音的分镜。"
            )

        else:
            progress_bar = st.progress(
                0
            )

            status_text = st.empty()

            audio_results = []

            errors = []

            total_scenes = len(
                scenes
            )

            for index, scene in enumerate(
                scenes
            ):
                scene_number = scene.get(
                    "scene_number",
                    index + 1,
                )

                try:
                    status_text.info(
                        f"正在生成镜头 "
                        f"{scene_number} 配音 "
                        f"({index + 1}/"
                        f"{total_scenes})..."
                    )

                    audio_result = (
                        generate_scene_audio_lazy(
                            scene
                        )
                    )

                    audio_key = str(
                        scene_number
                    )

                    st.session_state.scene_audio[
                        audio_key
                    ] = audio_result

                    audio_results.append(
                        audio_result
                    )

                except Exception as e:
                    errors.append(
                        (
                            scene_number,
                            str(e),
                        )
                    )

                progress_bar.progress(
                    (index + 1)
                    / total_scenes
                )

            # 所有音频成功后生成字幕
            if (
                not errors
                and len(audio_results)
                == total_scenes
            ):
                try:
                    status_text.info(
                        "正在根据真实音频时长"
                        "生成 SRT 字幕..."
                    )

                    subtitle_path = (
                        generate_srt_lazy(
                            audio_results
                        )
                    )

                    st.session_state.subtitle_path = (
                        subtitle_path
                    )

                    status_text.success(
                        "🎉 全部配音与字幕生成完成！"
                    )

                except Exception as e:
                    status_text.error(
                        "配音生成成功，"
                        "但字幕生成失败。"
                    )

                    with st.expander(
                        "查看字幕错误"
                    ):
                        st.code(
                            str(e)
                        )

            elif errors:
                status_text.warning(
                    "配音生成完成，"
                    "但部分镜头失败。"
                )

                with st.expander(
                    "查看 TTS 错误"
                ):
                    for (
                        scene_number,
                        error,
                    ) in errors:
                        st.markdown(
                            f"**镜头 "
                            f"{scene_number}**"
                        )

                        st.code(
                            error
                        )


    # =====================================================
    # 展示六个分镜
    # =====================================================
    st.divider()

    st.subheader("🎞️ 六个分镜")

    for scene in scenes:

        scene_number = scene.get(
            "scene_number",
            "",
        )

        visual = scene.get(
            "visual",
            "",
        )

        voiceover = scene.get(
            "voiceover",
            "",
        )

        sound = scene.get(
            "sound",
            "",
        )

        image_prompt = scene.get(
            "image_prompt",
            "",
        )

        video_prompt = scene.get(
            "video_prompt",
            "",
        )

        image_key = str(
            scene_number
        )

        audio_key = str(
            scene_number
        )

        with st.container(
            border=True
        ):

            st.markdown(
                f"### 镜头 {scene_number}"
            )

            # -------------------------
            # 画面
            # -------------------------
            st.markdown(
                "**🎨 画面**"
            )

            st.write(
                visual
            )

            # -------------------------
            # 旁白
            # -------------------------
            st.markdown(
                "**🎙️ 旁白**"
            )

            st.write(
                voiceover
            )

            # -------------------------
            # Sound
            # -------------------------
            st.markdown(
                "**🎵 音效 / BGM**"
            )

            st.write(
                sound
            )

            # -------------------------
            # Image Prompt
            # -------------------------
            st.markdown(
                "**🖼️ Image Prompt**"
            )

            st.code(
                image_prompt,
                language="text",
            )

            # -------------------------
            # Video Prompt
            # -------------------------
            st.markdown(
                "**🎥 Video Prompt**"
            )

            st.code(
                video_prompt,
                language="text",
            )

            # =================================================
            # 图片
            # =================================================
            st.markdown(
                "**🤖 AI 图片生成**"
            )

            current_image_path = (
                st.session_state.scene_images.get(
                    image_key
                )
            )

            current_image_exists = (
                current_image_path
                and Path(
                    current_image_path
                ).exists()
            )

            if current_image_exists:
                button_label = (
                    f"🔄 重新生成镜头 "
                    f"{scene_number} 图片"
                )

            else:
                button_label = (
                    f"🖼️ 生成镜头 "
                    f"{scene_number} 图片"
                )

            if st.button(
                button_label,
                key=(
                    f"generate_image_"
                    f"{scene_number}"
                ),
                use_container_width=True,
            ):
                try:
                    with st.spinner(
                        f"RTX 3060 正在生成镜头 "
                        f"{scene_number}..."
                    ):
                        image_path = (
                            generate_scene_image_lazy(
                                scene
                            )
                        )

                    st.session_state.scene_images[
                        image_key
                    ] = image_path

                    st.success(
                        f"镜头 {scene_number} "
                        f"图片生成成功！"
                    )

                except Exception as e:
                    st.error(
                        f"镜头 {scene_number} "
                        f"图片生成失败。"
                    )

                    with st.expander(
                        "查看图片生成错误"
                    ):
                        st.code(
                            str(e)
                        )

            image_path = (
                st.session_state.scene_images.get(
                    image_key
                )
            )

            if image_path:
                path = Path(
                    image_path
                )

                if path.exists():

                    st.image(
                        str(path),
                        caption=(
                            f"镜头 "
                            f"{scene_number}"
                        ),
                        use_container_width=True,
                    )

                    with open(
                        path,
                        "rb",
                    ) as image_file:

                        st.download_button(
                            label=(
                                f"⬇️ 下载镜头 "
                                f"{scene_number} 图片"
                            ),
                            data=(
                                image_file.read()
                            ),
                            file_name=(
                                path.name
                            ),
                            mime="image/png",
                            key=(
                                f"download_image_"
                                f"{scene_number}"
                            ),
                            use_container_width=True,
                        )

            # =================================================
            # 音频
            # =================================================
            st.markdown(
                "**🔊 AI 配音**"
            )

            audio_info = (
                st.session_state.scene_audio.get(
                    audio_key
                )
            )

            if audio_info:

                audio_path = audio_info.get(
                    "audio_path"
                )

                duration_value = audio_info.get(
                    "duration",
                    0,
                )

                if (
                    audio_path
                    and Path(
                        audio_path
                    ).exists()
                ):
                    audio_file_path = Path(
                        audio_path
                    )

                    audio_bytes = (
                        audio_file_path.read_bytes()
                    )

                    st.caption(
                        f"音频时长："
                        f"{duration_value:.2f} 秒"
                    )

                    st.audio(
                        audio_bytes,
                        format="audio/mpeg",
                    )

                    st.download_button(
                        label=(
                            f"⬇️ 下载镜头 "
                            f"{scene_number} 配音"
                        ),
                        data=audio_bytes,
                        file_name=(
                            audio_file_path.name
                        ),
                        mime="audio/mpeg",
                        key=(
                            f"download_audio_"
                            f"{scene_number}"
                        ),
                        use_container_width=True,
                    )


    # =====================================================
    # SRT 字幕
    # =====================================================
    subtitle_path = (
        st.session_state.subtitle_path
    )

    if subtitle_path:

        subtitle_file = Path(
            subtitle_path
        )

        if subtitle_file.exists():

            st.divider()

            st.subheader(
                "💬 SRT 字幕"
            )

            subtitle_text = (
                subtitle_file.read_text(
                    encoding="utf-8"
                )
            )

            st.code(
                subtitle_text,
                language="text",
            )

            st.download_button(
                label="💬 下载 SRT 字幕",
                data=(
                    subtitle_text.encode(
                        "utf-8"
                    )
                ),
                file_name="video.srt",
                mime="text/plain",
                use_container_width=True,
            )


    # =====================================================
    # 导出区域
    # =====================================================
    st.divider()

    st.subheader(
        "📤 导出生成结果"
    )

    json_data = {
        "metadata": (
            st.session_state.video_meta
        ),
        "video_plan": result,
        "generated_images": (
            st.session_state.scene_images
        ),
        "generated_audio": (
            st.session_state.scene_audio
        ),
        "subtitle_path": (
            st.session_state.subtitle_path
        ),
    }

    json_text = json.dumps(
        json_data,
        ensure_ascii=False,
        indent=2,
    )

    script_text = (
        build_script_text(
            result
        )
    )

    storyboard_text = (
        build_storyboard_markdown(
            result
        )
    )

    (
        download_col1,
        download_col2,
        download_col3,
    ) = st.columns(3)

    with download_col1:

        st.download_button(
            label="📦 下载完整 JSON",
            data=(
                json_text.encode(
                    "utf-8"
                )
            ),
            file_name=(
                "video_plan.json"
            ),
            mime=(
                "application/json"
            ),
            use_container_width=True,
        )

    with download_col2:

        st.download_button(
            label="📝 下载脚本文案",
            data=(
                script_text.encode(
                    "utf-8"
                )
            ),
            file_name=(
                "video_script.txt"
            ),
            mime="text/plain",
            use_container_width=True,
        )

    with download_col3:

        st.download_button(
            label="🎞️ 下载完整分镜",
            data=(
                storyboard_text.encode(
                    "utf-8"
                )
            ),
            file_name=(
                "storyboard.md"
            ),
            mime="text/markdown",
            use_container_width=True,
        )


# =========================
# 页脚
# =========================
st.divider()

st.caption(
    "当前版本：V0.9 · "
    "Ollama + Qwen3 4B + "
    "Stable Diffusion 1.5 + "
    "Batch Image Generation + "
    "Edge TTS + SRT Subtitle"
)