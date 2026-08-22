import streamlit as st

from ollama_service import generate_video_plan


st.set_page_config(
    page_title="AI Short Video Studio",
    page_icon="🎬",
    layout="wide",
)


st.title("🎬 AI Short Video Studio")
st.caption("把一个简单创意，快速变成结构化短视频方案。")


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


if st.button(
    "✨ 生成视频方案",
    type="primary",
    use_container_width=True,
):
    if not topic.strip():
        st.warning("先输入一个主题～")

    else:
        try:
            with st.spinner("AI 正在生成结构化短视频方案..."):
                result = generate_video_plan(
                    topic=topic,
                    style=style,
                    duration=duration,
                )

            st.success("生成完成！")
            st.divider()

            # 标题
            st.subheader("🎬 标题")
            st.write(result["title"])

            # Hook
            st.subheader("⚡ 前 3 秒 Hook")
            st.info(result["hook"])

            # 脚本
            st.subheader("📝 短视频脚本")
            st.write(result["script"])

            # 分镜
            st.subheader("🎞️ 六个分镜")

            scenes = result["scenes"]

            for scene in scenes:
                scene_number = scene.get("scene_number", "")
                visual = scene.get("visual", "")
                voiceover = scene.get("voiceover", "")
                sound = scene.get("sound", "")

                with st.container(border=True):
                    st.markdown(f"### 镜头 {scene_number}")

                    st.markdown("**画面**")
                    st.write(visual)

                    st.markdown("**旁白**")
                    st.write(voiceover)

                    st.markdown("**音效 / BGM**")
                    st.write(sound)

        except Exception as e:
            st.error("生成失败，请检查 Ollama 是否正在运行，或 AI 返回格式是否正确。")

            with st.expander("查看错误信息"):
                st.code(str(e))


st.divider()

st.caption(
    "当前版本：本地 Ollama + Qwen3 4B + JSON 结构化输出"
)