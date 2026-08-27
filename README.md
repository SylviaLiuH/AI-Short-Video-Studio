# 🎬 AI Short Video Studio

一个基于 **Python + Streamlit + Ollama** 的 AI 短视频创作工具。

用户输入主题、视频风格和时长，即可自动生成：

- 短视频标题
- 前 3 秒 Hook
- 完整短视频脚本
- 6 个结构化分镜
- 每个分镜的画面描述
- 每个分镜的旁白
- 每个分镜的音效 / BGM 建议
- 每个分镜对应的 Image Prompt
- 每个分镜对应的 Video Prompt
- 完整 JSON 导出
- 脚本文案导出
- 分镜 Markdown 导出

当前版本使用 **Ollama + Qwen3 4B** 在本地运行，无需依赖云端 LLM API 额度。

---

## ✨ 当前功能

### ✅ V0.1 — Streamlit 页面原型

- [x] 输入短视频主题
- [x] 选择视频风格
- [x] 选择视频时长
- [x] Mock 标题
- [x] Mock Hook
- [x] Mock 脚本
- [x] Mock 分镜

### ✅ V0.2 — 本地 LLM

- [x] 安装 Ollama
- [x] 本地运行 Qwen3 4B
- [x] Python 调用 Ollama Local API
- [x] Streamlit 接入真实 LLM
- [x] 根据用户主题实时生成内容

### ✅ V0.3 — JSON 结构化输出

- [x] JSON Structured Output
- [x] 关闭 Qwen3 Thinking 输出
- [x] Title 独立字段
- [x] Hook 独立字段
- [x] Script 独立字段
- [x] Scenes 独立字段
- [x] 固定生成 6 个分镜
- [x] Visual 独立字段
- [x] Voiceover 独立字段
- [x] Sound / BGM 独立字段
- [x] Streamlit 分模块展示

### ✅ V0.4 — Image Prompt / Video Prompt

- [x] 为每个分镜生成 Image Prompt
- [x] 为每个分镜生成 Video Prompt
- [x] Image Prompt 使用英文
- [x] Video Prompt 使用英文
- [x] Streamlit 展示视觉 Prompt
- [x] 为后续 AI 图片 / 视频生成提供结构化输入

### ✅ V0.5 — Export

- [x] 导出完整 JSON
- [x] 导出脚本文案
- [x] 导出完整分镜 Markdown
- [x] 保存用户主题
- [x] 保存视频风格
- [x] 保存视频时长
- [x] 使用 Session State 保存生成结果
- [x] 页面支持三个下载按钮

---

## 🧠 当前 AI Workflow

用户输入主题 / 风格 / 时长

↓

Streamlit

↓

Python

↓

Ollama Local API

↓

Qwen3 4B

↓

JSON Structured Output

↓

Python 解析 JSON

↓

Title / Hook / Script / Scenes

↓

Image Prompt / Video Prompt

↓

Streamlit 页面展示

↓

JSON / Script / Storyboard 导出

Ollama 默认运行在：

`http://127.0.0.1:11434`

---

## 📦 当前数据结构

短视频方案包含：

- `title`
- `hook`
- `script`
- `scenes`

每个 Scene 包含：

- `scene_number`
- `visual`
- `voiceover`
- `sound`
- `image_prompt`
- `video_prompt`

导出的 JSON 还包含：

- `topic`
- `style`
- `duration`

程序可以分别读取：

`result["title"]`

`result["hook"]`

`result["script"]`

`result["scenes"]`

以及：

`scene["image_prompt"]`

`scene["video_prompt"]`

这些结构化字段将作为后续 AI 图片生成、视频生成、配音和自动剪辑模块的输入。

---

## 📤 当前导出能力

项目当前支持三种导出格式。

### 完整 JSON

文件名：

`video_plan.json`

包含：

- Metadata
- Topic
- Style
- Duration
- Title
- Hook
- Script
- Scenes
- Image Prompt
- Video Prompt

主要用于后续程序继续处理。

### 脚本文案

文件名：

`video_script.txt`

包含：

- 标题
- Hook
- 完整脚本

适合人工修改、配音和内容发布准备。

### 完整分镜

文件名：

`storyboard.md`

包含：

- 标题
- Hook
- 完整脚本
- 六个分镜
- Visual
- Voiceover
- Sound / BGM
- Image Prompt
- Video Prompt

适合查看完整短视频制作方案。

---

## 🛠 技术栈

当前使用：

- Python
- Streamlit
- Requests
- JSON
- Ollama
- Qwen3 4B
- Git
- GitHub

后续计划使用：

- AI Image Generation
- TTS
- FFmpeg
- 自动字幕
- AI Video Generation
- AI Workflow
- Public Deployment

---

## 📁 项目结构

AI-Short-Video-Studio/

├── app.py  
├── ollama_service.py  
├── test_ollama.py  
├── test_api.py  
├── README.md  
├── .gitignore  
└── .env  

### app.py

Streamlit Web 应用入口。

负责：

- 接收用户主题
- 选择视频风格
- 选择视频时长
- 调用本地 AI 服务
- 展示结构化生成结果
- 保存 Session State
- 导出 JSON
- 导出 Script
- 导出 Storyboard

### ollama_service.py

本地 LLM 服务模块。

负责：

Python  
↓  
Ollama Local API  
↓  
Qwen3 4B  
↓  
JSON Structured Output  
↓  
Python Dictionary

并生成：

- Title
- Hook
- Script
- Scenes
- Image Prompt
- Video Prompt

### test_ollama.py

用于测试：

`Python → Ollama API → Qwen3`

是否可以正常连接。

### test_api.py

用于测试云端 LLM API。

当前项目主要使用本地 Ollama，因此不依赖云端 LLM API 额度。

---

## 🚀 本地运行

### 1. 安装 Python 依赖

运行：

`py -m pip install streamlit requests`

### 2. 安装 Ollama

安装完成后检查：

`ollama --version`

### 3. 下载并运行本地模型

当前使用：

`ollama run qwen3:4b`

首次运行时 Ollama 会自动下载模型。

模型可以正常回复后，可以输入：

`/bye`

退出命令行聊天。

Ollama 服务仍然可以继续在后台提供 Local API。

### 4. 启动项目

在项目根目录运行：

`py -m streamlit run app.py`

浏览器访问：

`http://localhost:8501`

---

## 🎬 使用示例

输入主题：

> 一只猫发现家里的镜子通往另一个世界

选择：

- 视频风格：奇幻
- 视频时长：30 秒

系统自动生成：

标题

↓

前 3 秒 Hook

↓

完整短视频脚本

↓

6 个结构化分镜

↓

每个分镜的画面 / 旁白 / 音效

↓

Image Prompt

↓

Video Prompt

↓

JSON / Script / Storyboard 导出

---

## 🎯 项目目标

AI Short Video Studio 希望探索一套完整的 AI 短视频生产 Workflow：

主题输入

↓

LLM 生成标题 / Hook / Script

↓

结构化分镜

↓

Image Prompt / Video Prompt

↓

AI 图片

↓

TTS 配音

↓

自动字幕

↓

FFmpeg 视频合成

↓

最终短视频

最终希望将一个简单创意，转化为一套可以重复使用的 AI 内容生产流程。

项目同时用于实践：

- Vibe Coding
- LLM Application Development
- API 调用
- Local AI Deployment
- JSON Structured Output
- Prompt Engineering
- AI Workflow
- Web App Development
- 自动化内容生产

---

## 🗺 Roadmap

### ✅ 已完成

- [x] V0.1 Streamlit 页面原型
- [x] V0.2 Ollama + Qwen3 本地 LLM
- [x] V0.3 JSON Structured Output
- [x] V0.4 Image Prompt / Video Prompt
- [x] V0.5 Export

### 🔜 V0.6 — AI 图片生成

- [ ] 接入 AI 图片生成能力
- [ ] 使用 Image Prompt 生成图片
- [ ] 至少成功生成一个真实分镜图片
- [ ] 保存生成图片
- [ ] 在 Streamlit 页面展示图片

### 🔜 V0.7 — Batch Image Generation

- [ ] 自动处理六个 Image Prompt
- [ ] 批量生成六张分镜图片
- [ ] 自动命名图片
- [ ] 保存图片路径

### 🔜 V0.8 — TTS

- [ ] Script / Voiceover 转语音
- [ ] 保存音频文件
- [ ] Streamlit 播放音频

### 🔜 V0.9 — Subtitle + Video Composition

- [ ] 生成字幕文件
- [ ] 接入 FFmpeg
- [ ] 图片 + 音频 + 字幕合成
- [ ] 输出 MP4

### 🔜 V1.0 — Complete Workflow

- [ ] Topic
- [ ] Script
- [ ] Storyboard
- [ ] Image Prompt
- [ ] Images
- [ ] Voice
- [ ] Subtitle
- [ ] Video
- [ ] Export
- [ ] 完整 Workflow 跑通

---

## 🔐 安全说明

`.env` 已加入 `.gitignore`。

请不要将以下内容上传到 GitHub：

- API Key
- Token
- 密码
- Cookie
- 其他敏感凭据

当前主要 LLM 服务运行在本机：

`127.0.0.1:11434`

文本和 Prompt 生成流程可以在本地完成。

---

## 📌 当前版本

**V0.5**

当前状态：

> ✅ Streamlit + Ollama + Qwen3 4B + JSON Structured Output + Image Prompt + Video Prompt + Export 已跑通。

下一步：

> 🖼️ 接入 AI 图片生成能力，让至少一个分镜真正生成图片。