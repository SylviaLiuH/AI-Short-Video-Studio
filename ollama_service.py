import json

import requests


OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "qwen3:4b"


def generate_video_plan(
    topic: str,
    style: str,
    duration: str,
) -> dict:

    prompt = f"""
你是一名专业的短视频编剧。

请根据以下信息生成短视频方案：

主题：{topic}
风格：{style}
时长：{duration}

你必须严格输出 JSON。

JSON 格式如下：

{{
    "title": "短视频标题",
    "hook": "前3秒吸引观众的Hook",
    "script": "完整短视频旁白/脚本",
    "scenes": [
        {{
            "scene_number": 1,
            "visual": "画面描述",
            "voiceover": "这一镜的旁白",
            "sound": "音效或背景音乐建议"
        }},
        {{
            "scene_number": 2,
            "visual": "画面描述",
            "voiceover": "这一镜的旁白",
            "sound": "音效或背景音乐建议"
        }}
    ]
}}

要求：

1. scenes 必须正好有 6 个分镜
2. 使用中文
3. 内容符合用户指定的主题、风格和时长
4. Hook 要适合短视频前 3 秒
5. 每个 visual 要具体，方便以后用于 AI 图片和视频生成
6. 不要输出 Markdown
7. 不要输出 ```json
8. 不要解释
9. 只返回合法 JSON
"""

    session = requests.Session()

    # 避免本机代理影响 localhost 请求
    session.trust_env = False

    response = session.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "think": False,
            "format": "json",
            "options": {
                "temperature": 0,
            },
        },
        timeout=180,
    )

    response.raise_for_status()

    result = response.json()

    raw_text = result["response"]

    try:
        video_plan = json.loads(raw_text)

    except json.JSONDecodeError as e:
        raise ValueError(
            f"AI 返回的内容不是合法 JSON。\n\n原始输出：\n{raw_text}"
        ) from e

    return video_plan