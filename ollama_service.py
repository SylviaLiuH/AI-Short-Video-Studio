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
你是一名专业的短视频编剧和 AI 视觉提示词设计师。

请根据以下信息生成一个结构化的短视频方案：

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
            "sound": "音效或背景音乐建议",
            "image_prompt": "用于 AI 图片生成的英文提示词",
            "video_prompt": "用于 AI 视频生成的英文提示词"
        }}
    ]
}}

要求：

1. scenes 必须正好有 6 个分镜
2. 使用中文生成 title、hook、script、visual、voiceover、sound
3. image_prompt 和 video_prompt 必须使用英文
4. 内容符合用户指定的主题、风格和时长
5. Hook 要适合短视频前 3 秒
6. 每个 visual 要具体，方便以后用于 AI 图片和视频生成
7. image_prompt 要适合静态画面生成，要突出：
   - 主体
   - 场景
   - 光线
   - 氛围
   - 构图
   - 风格
8. video_prompt 要适合视频生成，要突出：
   - 主体动作
   - 镜头运动
   - 场景变化
   - 光线
   - 情绪氛围
   - 画面风格
9. image_prompt 和 video_prompt 要尽量具体、自然、可直接给生图/生视频模型使用
10. 不要输出 Markdown
11. 不要输出 ```json
12. 不要解释
13. 只返回合法 JSON
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