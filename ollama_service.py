import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "qwen3:4b"


def generate_video_plan(topic: str, style: str, duration: str) -> str:
    prompt = f"""
你是一名短视频编剧。

请根据下面的信息设计一个短视频方案。

主题：{topic}
风格：{style}
时长：{duration}

请生成：

1. 一个吸引人的标题
2. 一个前3秒 Hook
3. 一份短视频脚本
4. 六个分镜

要求：
- 使用中文
- 内容紧凑
- 适合短视频
- 不要解释你的思考过程
"""

    session = requests.Session()
    session.trust_env = False

    response = session.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=180,
    )

    response.raise_for_status()

    result = response.json()

    return result["response"]