import streamlit as st

st.set_page_config(
    page_title="AI Short Video Studio",
    page_icon="🎬",
    layout="wide",
)

st.title("🎬 AI Short Video Studio")
st.caption("Turn one idea into a short-video concept.")

topic = st.text_area(
    "你想做什么内容？",
    placeholder="例如：一个女孩捡到了一只会说话的黑猫",
    height=100,
)

style = st.selectbox(
    "视频风格",
    ["悬疑", "治愈", "搞笑", "奇幻", "情绪故事"],
)

duration = st.selectbox(
    "视频时长",
    ["30 秒", "45 秒", "60 秒"],
)

if st.button("✨ 生成视频方案", type="primary"):
    if not topic.strip():
        st.warning("先输入一个主题～")
    else:
        st.subheader("标题")
        st.write("《她捡回家的黑猫，竟然知道她所有的秘密》")

        st.subheader("Hook")
        st.info("她只是捡了一只流浪猫。直到那天晚上，它突然叫出了她的名字。")

        st.subheader("短视频脚本")
        st.write(
            """
            雨夜里，她在楼下发现了一只浑身湿透的黑猫。

            她把猫抱回家，擦干身体，给它准备了一小碗食物。

            凌晨两点，她被客厅里的声音惊醒。

            “别开那扇门。”

            她愣住了。

            房间里只有她，和那只正在盯着她看的黑猫。
            """
        )

        st.subheader("🎞️ 六个分镜")

        scenes = [
            "镜头 1：雨夜街道，女孩发现蜷缩在纸箱里的黑猫。",
            "镜头 2：女孩抱着湿漉漉的黑猫回到公寓。",
            "镜头 3：暖黄色灯光下，黑猫安静地吃东西。",
            "镜头 4：凌晨两点，女孩突然从床上醒来。",
            "镜头 5：黑暗客厅中，黑猫抬头看着女孩。",
            "镜头 6：门把手缓缓转动，黑猫说：别开门。",
        ]

        for scene in scenes:
            st.write(scene)