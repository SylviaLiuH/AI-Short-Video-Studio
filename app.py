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
# 页面标题
# =========================
st.title("🎬 AI Short Video Studio")
st.caption("把一个简单的创意，快速变成短视频脚本与分镜方案。")


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

    # 没有输入主题
    if not topic.strip():
        st.warning("先输入一个主题～")

    else:
        try:
            with st.spinner("AI 正在生成短视频方案..."):

                result = generate_video_plan(
                    topic=topic,
                    style=style,
                    duration=duration,
                )

            # =========================
            # 输出区域
            # =========================
            st.success("生成完成！")

            st.divider()

            st.subheader("🎬 AI 生成结果")

            st.markdown(result)

        except Exception as e:
            st.error("生成失败，请检查 Ollama 是否正在运行。")

            with st.expander("查看错误信息"):
                st.code(str(e))


# =========================
# 页面底部说明
# =========================
st.divider()

st.caption(
    "当前版本使用本地 Ollama + Qwen3 生成内容，"
    "无需云端 LLM API 额度。"
)