import json

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


# =========================
# 导出函数
# =========================
def build_script_text(result: dict) -> str:
    """导出标题、Hook 和完整脚本。"""

    return f"""AI Short Video Studio

标题：
{result.get("title", "")}

前 3 秒 Hook：
{result.get("hook", "")}

完整脚本：
{result.get("script", "")}
"""


def build_storyboard_markdown(result: dict) -> str:
    """把所有分镜整理成 Markdown 文本。"""

    lines = [
        "# AI Short Video Storyboard",
        "",
        f"## 标题",
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
        scene_number = scene.get("scene_number", "")

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
    "把一个简单创意，快速变成结构化短视频方案。"
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
# 生成按钮
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

            # 保存到 session_state
            st.session_state.video_plan = result

            st.session_state.video_meta = {
                "topic": topic,
                "style": style,
                "duration": duration,
            }

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

    # -------------------------
    # 标题
    # -------------------------
    st.subheader("🎬 标题")
    st.write(result.get("title", ""))

    # -------------------------
    # Hook
    # -------------------------
    st.subheader("⚡ 前 3 秒 Hook")
    st.info(result.get("hook", ""))

    # -------------------------
    # 脚本
    # -------------------------
    st.subheader("📝 短视频脚本")
    st.write(result.get("script", ""))

    # -------------------------
    # 分镜
    # -------------------------
    st.subheader("🎞️ 六个分镜")

    scenes = result.get("scenes", [])

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

        with st.container(border=True):

            st.markdown(
                f"### 镜头 {scene_number}"
            )

            st.markdown("**🎨 画面**")
            st.write(visual)

            st.markdown("**🎙️ 旁白**")
            st.write(voiceover)

            st.markdown("**🎵 音效 / BGM**")
            st.write(sound)

            st.markdown("**🖼️ Image Prompt**")
            st.code(
                image_prompt,
                language="text",
            )

            st.markdown("**🎥 Video Prompt**")
            st.code(
                video_prompt,
                language="text",
            )


    # =========================
    # 导出区域
    # =========================
    st.divider()

    st.subheader("📤 导出生成结果")

    # 完整 JSON
    json_text = json.dumps(
        {
            "metadata": st.session_state.video_meta,
            "video_plan": result,
        },
        ensure_ascii=False,
        indent=2,
    )

    # 脚本文本
    script_text = build_script_text(
        result
    )

    # 分镜 Markdown
    storyboard_text = build_storyboard_markdown(
        result
    )

    download_col1, download_col2, download_col3 = st.columns(3)

    with download_col1:

        st.download_button(
            label="📦 下载完整 JSON",
            data=json_text.encode("utf-8"),
            file_name="video_plan.json",
            mime="application/json",
            use_container_width=True,
        )

    with download_col2:

        st.download_button(
            label="📝 下载脚本文案",
            data=script_text.encode("utf-8"),
            file_name="video_script.txt",
            mime="text/plain",
            use_container_width=True,
        )

    with download_col3:

        st.download_button(
            label="🎞️ 下载完整分镜",
            data=storyboard_text.encode("utf-8"),
            file_name="storyboard.md",
            mime="text/markdown",
            use_container_width=True,
        )


# =========================
# 页脚
# =========================
st.divider()

st.caption(
    "当前版本：V0.5 · "
    "Ollama + Qwen3 4B + JSON Structured Output + "
    "Image / Video Prompt + Export"
)