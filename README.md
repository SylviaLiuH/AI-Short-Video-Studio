# 🎬 AI Short Video Studio

一个基于 **Python + Streamlit + Ollama + 本地大语言模型** 的 AI 短视频内容生成工具。

用户输入一个主题，并选择视频风格和时长后，系统可以通过本地 LLM 自动生成结构化的短视频方案，包括：

- 视频标题
- 前 3 秒 Hook
- 完整短视频脚本
- 6 个结构化分镜
- 每个分镜的画面描述
- 每个分镜的旁白
- 每个分镜的音效 / BGM 建议

当前版本使用 **Ollama + Qwen3 4B** 在本地运行，无需依赖云端 LLM API 额度。

---

## ✨ 当前功能

### V0.3

目前已经支持：

- [x] 输入短视频主题
- [x] 选择视频风格
- [x] 选择视频时长
- [x] Streamlit Web 页面
- [x] 本地部署 Ollama
- [x] 本地运行 Qwen3 4B
- [x] Python 调用 Ollama Local API
- [x] 根据用户输入实时生成短视频内容
- [x] JSON Structured Output
- [x] 独立提取视频标题
- [x] 独立提取前 3 秒 Hook
- [x] 独立提取完整脚本
- [x] 独立提取 6 个分镜
- [x] 每个分镜包含画面、旁白、音效 / BGM
- [x] Streamlit 分模块展示结构化结果

---

## 🧠 AI Workflow

当前的生成流程：

```text
用户输入主题 / 风格 / 时长
          ↓
     Streamlit 页面
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
Streamlit 分模块展示
```

Ollama 默认运行在：

```text
http://127.0.0.1:11434
```

---

## 📦 JSON 数据结构

当前 LLM 返回的数据结构类似：

```json
{
  "title": "短视频标题",
  "hook": "前3秒Hook",
  "script": "完整短视频脚本",
  "scenes": [
    {
      "scene_number": 1,
      "visual": "画面描述",
      "voiceover": "旁白",
      "sound": "音效或BGM建议"
    }
  ]
}
```

程序会将 JSON 转换为 Python Dictionary，从而可以分别读取：

```python
result["title"]
result["hook"]
result["script"]
result["scenes"]
```

这为后续自动生成图片、视频、配音和字幕提供结构化数据基础。

---

## 🛠 技术栈

### 当前使用

- Python
- Streamlit
- Requests
- JSON
- Ollama
- Qwen3 4B
- Git / GitHub

### 后续计划

- Prompt Engineering
- AI Image Generation
- AI Video Generation
- TTS
- FFmpeg
- 自动字幕
- AI Workflow
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

#### `app.py`

Streamlit Web 应用入口。

负责：

- 接收主题
- 选择视频风格
- 选择视频时长
- 调用 AI 服务
- 展示结构化生成结果

---

#### `ollama_service.py`

本地 LLM 服务模块。

负责：

```text
Python
↓
Ollama Local API
↓
Qwen3 4B
↓
JSON
↓
Python Dictionary
```

同时负责 Prompt 和 JSON 解析。

---

#### `test_ollama.py`

用于测试：

```text
Python → Ollama API → Qwen3
```

是否可以正常连接。

---

#### `test_api.py`

用于测试云端 LLM API。

由于当前云端 API 账户没有可用 Credits，项目主要使用本地 Ollama。

---

## 🚀 本地运行

### 1. 安装 Python 依赖

```bash
py -m pip install streamlit requests
```

---

### 2. 安装 Ollama

安装后检查：

```bash
ollama --version
```

---

### 3. 下载 Qwen3 4B

```bash
ollama run qwen3:4b
```

首次运行会自动下载模型。

下载完成并测试模型后，可以输入：

```text
/bye
```

退出命令行聊天。

Ollama 服务仍可以继续在后台提供 Local API。

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
一个女孩在旧相机里发现了未来的照片
```

选择：

```text
视频风格：奇幻
视频时长：30 秒
```

系统会自动生成：

```text
标题
↓
前 3 秒 Hook
↓
完整短视频脚本
↓
6 个分镜
   ├─ 画面
   ├─ 旁白
   └─ 音效 / BGM
```

---

## 🗺 开发记录

### ✅ V0.1 — Streamlit 原型

完成：

- [x] Streamlit 页面
- [x] 主题输入
- [x] 风格选择
- [x] 时长选择
- [x] Mock 标题
- [x] Mock Hook
- [x] Mock 脚本
- [x] Mock 分镜

这一阶段主要用于验证产品页面和基本交互流程。

---

### ✅ V0.2 — 本地 LLM

完成：

- [x] 安装 Ollama
- [x] 下载并运行 Qwen3 4B
- [x] Python 调用 Ollama Local API
- [x] Streamlit 接入真实 LLM
- [x] 根据用户主题实时生成内容

这一阶段将 Mock 数据替换为真实 AI 生成内容。

---

### ✅ V0.3 — JSON 结构化输出

完成：

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

现在程序已经可以真正理解和处理 AI 返回的数据，而不再只是显示一整段文本。

---

## 🔜 下一阶段

### V0.4 — AI 图片 / 视频 Prompt

计划：

- [ ] 根据每个 `visual` 自动生成 AI 图片 Prompt
- [ ] 自动生成 AI 视频 Prompt
- [ ] 增加镜头语言
- [ ] 增加景别
- [ ] 增加人物一致性描述
- [ ] 增加画面风格描述
- [ ] 为后续 Runway / 图片模型准备输入

---

### 后续版本

- [ ] AI 图片生成
- [ ] AI 视频生成
- [ ] TTS AI 配音
- [ ] 自动字幕
- [ ] FFmpeg 视频合成
- [ ] 图片 / 视频 / 配音 / 字幕自动化 Workflow
- [ ] 一键生成完整短视频
- [ ] 公网部署
- [ ] 内容模板系统
- [ ] 多种短视频类型
- [ ] 内容生产批量化

---

## 🎯 项目目标

AI Short Video Studio 希望探索一套完整的 AI 短视频生产 Workflow：

```text
主题
↓
LLM
↓
标题 / Hook / Script
↓
结构化分镜
↓
Image Prompt / Video Prompt
↓
AI 图片 / AI 视频
↓
TTS 配音
↓
字幕
↓
视频合成
↓
最终短视频
```

最终希望将一个简单的创意，转化为一套可以重复使用的 AI 内容生产流程。

这个项目也用于实践：

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

## 🔐 安全说明

`.env` 已加入 `.gitignore`。

请不要将：

- API Key
- Token
- 密码
- Cookie
- 其他敏感凭据

上传到 GitHub。

当前主要 LLM 运行在本机：

```text
127.0.0.1:11434
```

短视频文本生成流程可以在本地完成。

---

## 📌 当前版本

**V0.3**

当前状态：

> ✅ Streamlit + Ollama + Qwen3 4B + JSON Structured Output 已跑通。

下一步：

> 🎨 **为每个分镜自动生成 AI 图片 Prompt 和视频 Prompt。**