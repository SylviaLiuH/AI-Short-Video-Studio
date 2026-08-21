# 🎬 AI Short Video Studio

一个基于 **Python + Streamlit + 本地大语言模型** 的 AI 短视频内容生成工具。

用户只需要输入一个主题，并选择视频风格和时长，系统就可以自动生成：

- 短视频标题
- 前 3 秒 Hook
- 短视频脚本
- 6 个分镜方案

当前版本使用 **Ollama + Qwen3 4B** 在本地运行大语言模型，无需消耗云端 LLM API 额度。

---

## ✨ 当前功能

### V0.2

目前已经支持：

- [x] 输入短视频主题
- [x] 选择视频风格
- [x] 选择视频时长
- [x] Streamlit Web 页面
- [x] 本地部署 Ollama
- [x] 本地运行 Qwen3 4B
- [x] Python 调用 Ollama Local API
- [x] 根据用户输入实时生成内容
- [x] 自动生成短视频标题
- [x] 自动生成前 3 秒 Hook
- [x] 自动生成短视频脚本
- [x] 自动生成 6 个分镜

V0.1 使用固定 Mock 数据完成页面原型。

V0.2 已经接入真实本地 LLM，生成结果会根据用户输入的主题、风格和时长实时变化。

---

## 🧠 当前 AI Workflow

目前的调用流程：

```text
用户输入主题
    ↓
Streamlit 页面
    ↓
Python
    ↓
Ollama Local API
    ↓
Qwen3 4B
    ↓
生成短视频方案
    ↓
Streamlit 页面展示结果
```

Ollama 默认运行在：

```text
http://127.0.0.1:11434
```

---

## 🛠 技术栈

### 当前使用

- Python
- Streamlit
- Requests
- Ollama
- Qwen3 4B
- Git / GitHub

### 后续计划

- JSON Structured Output
- AI Image Generation
- TTS
- FFmpeg
- Video Generation API
- Local AI Workflow
- Public Deployment

---

## 📁 项目结构

```text
AI-Short-Video-Studio/
│
├─ app.py
├─ ollama_service.py
├─ test_ollama.py
├─ test_api.py
├─ README.md
├─ .gitignore
└─ .env
```

### 文件说明

`app.py`

Streamlit Web 应用入口，负责用户输入和生成结果展示。

`ollama_service.py`

负责调用本地 Ollama API，并将主题、风格、时长发送给本地大语言模型。

`test_ollama.py`

用于测试：

```text
Python → Ollama API → Qwen3
```

是否可以正常连接。

`test_api.py`

用于测试云端 LLM API。

当前主要版本使用本地 Ollama，不依赖云端 API 额度。

---

## 🚀 本地运行

### 1. 安装 Python 依赖

```bash
py -m pip install streamlit requests
```

---

### 2. 安装 Ollama

安装 Ollama 后确认：

```bash
ollama --version
```

---

### 3. 下载并运行本地模型

当前使用：

```bash
ollama run qwen3:4b
```

首次运行时 Ollama 会自动下载模型。

模型下载完成并确认可以正常对话后，可以使用：

```text
/bye
```

退出命令行聊天。

Ollama 服务仍然可以在后台提供 Local API。

---

### 4. 启动 AI Short Video Studio

在项目根目录运行：

```bash
py -m streamlit run app.py
```

浏览器访问：

```text
http://localhost:8501
```

---

## 🎬 使用示例

输入：

```text
一个机器人第一次看到大海
```

选择：

```text
视频风格：治愈
视频时长：30 秒
```

系统可以实时生成：

```text
标题
↓
前 3 秒 Hook
↓
短视频脚本
↓
6 个分镜
```

生成内容来自本地运行的 Qwen3 4B，而不是预先写死的 Mock 数据。

---

## 🗺 开发计划

### ✅ V0.1 — 页面原型

- [x] Streamlit 页面
- [x] 主题输入
- [x] 风格选择
- [x] 时长选择
- [x] Mock 标题
- [x] Mock Hook
- [x] Mock 脚本
- [x] Mock 分镜

### ✅ V0.2 — 本地 LLM

- [x] 安装 Ollama
- [x] 本地运行 Qwen3 4B
- [x] 调用 Ollama Local API
- [x] Streamlit 接入真实 LLM
- [x] 根据主题实时生成内容

### 🔜 V0.3 — 结构化输出

- [ ] JSON Structured Output
- [ ] 独立提取 Title
- [ ] 独立提取 Hook
- [ ] 独立提取 Script
- [ ] 独立提取 Storyboard
- [ ] 分镜数据结构化

### 🔜 后续版本

- [ ] AI 图片 Prompt 自动生成
- [ ] AI 视频 Prompt 自动生成
- [ ] AI 图片生成
- [ ] AI 视频生成
- [ ] TTS AI 配音
- [ ] 自动字幕生成
- [ ] FFmpeg 视频合成
- [ ] 图片 / 视频 / 配音 / 字幕自动化 Workflow
- [ ] 一键生成完整短视频
- [ ] 公网部署
- [ ] 内容模板与风格系统

---

## 🎯 项目目标

AI Short Video Studio 希望探索一套完整的 AI 短视频生产 Workflow：

```text
主题输入
    ↓
LLM 生成 Hook / 标题 / 脚本
    ↓
结构化分镜
    ↓
AI 图片 Prompt
    ↓
AI 图片 / 视频生成
    ↓
AI 配音
    ↓
自动字幕
    ↓
视频自动合成
    ↓
最终短视频
```

最终希望将一个简单的创意，快速转化为一套可以继续生成图片、视频、配音和字幕的短视频生产方案。

这个项目也用于实践：

- Vibe Coding
- LLM Application Development
- API 调用
- 本地 AI 部署
- Prompt Engineering
- AI Workflow
- Web App Development
- 自动化内容生产

---

## 🔐 安全说明

`.env` 已加入 `.gitignore`。

请不要将 API Key、Token 或其他敏感凭据上传至 GitHub。

当前 Ollama Local API 运行在本机：

```text
127.0.0.1:11434
```

主要内容生成流程可以在本地完成。

---

## 📌 当前版本

**V0.2**

当前状态：

> ✅ Streamlit + Ollama + Qwen3 4B 本地 AI 短视频脚本生成流程已跑通。

下一步：

> **JSON 结构化输出。**