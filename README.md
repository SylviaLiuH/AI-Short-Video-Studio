# 🎬 AI Short Video Studio

一个基于 **Python + Streamlit + Ollama + Stable Diffusion + Edge TTS** 的 AI 短视频创作工具。

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
- 6 张 AI 分镜图片
- 6 段 AI 配音
- 自动 SRT 字幕
- JSON / Script / Storyboard 导出
- 图片 / 音频 / 字幕下载

当前文本生成使用：

`Ollama + Qwen3 4B`

当前图片生成使用：

`Stable Diffusion 1.5 + PyTorch + CUDA + NVIDIA GPU`

当前语音生成使用：

`Edge TTS`

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

### ✅ V0.3 — JSON Structured Output

- [x] AI 严格输出 JSON
- [x] 关闭 Qwen3 Thinking
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
- [x] 为 AI 图片与视频生成准备结构化输入

### ✅ V0.5 — Export

- [x] 导出完整 JSON
- [x] 导出脚本文案
- [x] 导出完整分镜 Markdown
- [x] 保存 Topic
- [x] 保存 Style
- [x] 保存 Duration
- [x] 使用 Session State 保存结果
- [x] Streamlit 下载按钮

### ✅ V0.6 — Local AI Image Generation

- [x] CUDA 版本 PyTorch
- [x] Python 成功调用 NVIDIA GPU
- [x] Hugging Face Diffusers
- [x] Stable Diffusion 1.5
- [x] Image Prompt → PNG
- [x] 图片自动保存
- [x] 单分镜图片生成测试成功
- [x] 本地 GPU 生图 Workflow 跑通

### ✅ V0.7 — Streamlit Image Generation

- [x] image_service 接入 Streamlit
- [x] 单分镜生成图片
- [x] 页面展示生成图片
- [x] 图片路径保存到 Session State
- [x] 图片下载
- [x] generated_images 写入 JSON
- [x] Web Image Generation Workflow 跑通

### ✅ V0.8 — Batch Image Generation

- [x] 一键生成全部 6 个分镜图片
- [x] 自动读取 Image Prompt
- [x] 顺序调用 Stable Diffusion
- [x] 自动跳过已有图片
- [x] 显示生成进度
- [x] 保存全部图片路径
- [x] 页面展示 6 张图片
- [x] 单镜头重新生成
- [x] Batch Image Workflow 跑通

### ✅ V0.9 — TTS + Subtitle

- [x] 接入 Edge TTS
- [x] Voiceover 转 MP3
- [x] 单镜头 TTS 测试
- [x] 批量生成 6 段配音
- [x] 自动保存音频文件
- [x] 使用 Mutagen 获取真实音频时长
- [x] 根据音频时长自动生成字幕时间轴
- [x] 自动生成 SRT
- [x] Streamlit 一键生成全部配音与字幕
- [x] 页面直接播放 MP3
- [x] 单段音频下载
- [x] SRT 页面展示
- [x] SRT 文件下载
- [x] Audio / Subtitle 信息写入导出 JSON

---

## 🧠 当前完整 Workflow

用户输入：

Topic / Style / Duration

↓

Streamlit

↓

Ollama Local API

↓

Qwen3 4B

↓

JSON Structured Output

↓

Title / Hook / Script

↓

6 个 Scenes

↓

Visual / Voiceover / Sound

↓

Image Prompt / Video Prompt

↓

Stable Diffusion 1.5

↓

PyTorch + CUDA

↓

NVIDIA GPU

↓

6 张分镜 PNG

↓

Voiceover

↓

Edge TTS

↓

6 段 MP3

↓

Mutagen 读取真实音频时长

↓

自动计算字幕时间轴

↓

生成 SRT

↓

Streamlit 展示 / 播放 / 下载

目前已经完成：

`Topic → Script → Storyboard → Images → Voice → Subtitle`

下一步：

`Images + Voice + Subtitle → FFmpeg → MP4`

---

## 🤖 本地 AI 模型

### 文本生成

模型：

`qwen3:4b`

运行方式：

`Ollama`

默认 API：

`http://127.0.0.1:11434`

负责：

- Title
- Hook
- Script
- Scenes
- Image Prompt
- Video Prompt

### 图片生成

模型：

`runwayml/stable-diffusion-v1-5`

运行框架：

- PyTorch
- Diffusers
- Transformers
- Accelerate
- CUDA

测试设备：

`NVIDIA GeForce RTX 3060 Laptop GPU`

显存：

`6 GB VRAM`

默认图片尺寸：

`512 × 512`

---

## 🔊 TTS 配音

TTS 模块位于：

`tts_service.py`

当前使用：

`Edge TTS`

默认中文声音：

`zh-CN-XiaoxiaoNeural`

主要流程：

Voiceover

↓

Edge TTS

↓

MP3

↓

Mutagen

↓

获取真实音频时长

音频默认保存到：

`outputs/audio/`

例如：

`outputs/audio/scene_1.mp3`

`outputs/audio/scene_2.mp3`

一直到：

`outputs/audio/scene_6.mp3`

Edge TTS 需要联网使用。

---

## 💬 SRT 字幕

字幕由 `tts_service.py` 自动生成。

程序读取每个 Scene 的：

- voiceover
- audio duration

并按顺序计算时间轴。

流程：

Scene 1 Audio Duration

↓

Scene 2 Start Time

↓

Scene 2 Audio Duration

↓

Scene 3 Start Time

↓

...

↓

完整时间轴

↓

SRT

默认输出：

`outputs/subtitles/video.srt`

示例结构：

1

00:00:00,000 --> 00:00:03,200

第一段旁白

2

00:00:03,200 --> 00:00:06,800

第二段旁白

---

## 📦 当前数据结构

视频方案包含：

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

Metadata 包含：

- `topic`
- `style`
- `duration`

生成图片后保存：

- `generated_images`

生成配音后保存：

- `generated_audio`

生成字幕后保存：

- `subtitle_path`

这些数据将作为 V1.0 视频合成模块的输入。

---

## 📤 导出能力

### JSON

文件：

`video_plan.json`

包含：

- Metadata
- Video Plan
- Scenes
- Image Prompt
- Video Prompt
- Generated Images
- Generated Audio
- Subtitle Path

### Script

文件：

`video_script.txt`

包含：

- Title
- Hook
- Script

### Storyboard

文件：

`storyboard.md`

包含：

- Script
- 6 Scenes
- Visual
- Voiceover
- Sound
- Image Prompt
- Video Prompt

### Images

格式：

`PNG`

可以在 Streamlit 页面单独下载。

### Audio

格式：

`MP3`

每个 Scene 的配音可以单独播放和下载。

### Subtitle

格式：

`SRT`

可以直接在 Streamlit 页面下载。

---

## 🛠 技术栈

当前使用：

- Python
- Streamlit
- Requests
- JSON
- Ollama
- Qwen3 4B
- PyTorch
- CUDA
- Diffusers
- Transformers
- Accelerate
- Safetensors
- Pillow
- Stable Diffusion 1.5
- Edge TTS
- Mutagen
- Git
- GitHub

下一阶段：

- FFmpeg
- Video Composition

后续计划：

- AI Video Generation
- Public Deployment
- Docker
- 更完整的任务管理
- 更成熟的项目架构

---

## 📁 项目结构

AI-Short-Video-Studio/

├── app.py
├── ollama_service.py
├── image_service.py
├── tts_service.py
├── test_ollama.py
├── test_api.py
├── test_image.py
├── test_tts.py
├── test_tts_batch.py
├── README.md
├── .gitignore
├── .env
└── outputs/
    ├── images/
    ├── audio/
    └── subtitles/

### app.py

Streamlit Web App。

负责：

- 用户输入
- 视频方案生成
- Scene 展示
- 图片生成
- 批量图片生成
- TTS
- Subtitle
- Audio Player
- 下载
- Session State
- 数据导出

### ollama_service.py

负责：

`Python → Ollama → Qwen3 → Structured JSON`

### image_service.py

负责：

`Image Prompt → Stable Diffusion → CUDA → PNG`

### tts_service.py

负责：

`Voiceover → Edge TTS → MP3 → Duration → SRT`

### test_ollama.py

测试：

`Python → Ollama`

### test_image.py

测试：

`Python → Stable Diffusion → CUDA → PNG`

### test_tts.py

测试：

`Text → Edge TTS → MP3`

### test_tts_batch.py

测试：

`6 Voiceovers → 6 MP3 → SRT`

### test_api.py

用于测试云端 LLM API。

当前核心文本生成流程使用本地 Ollama。

---

## 🚀 本地运行

### 1. 基础依赖

`py -m pip install streamlit requests`

### 2. Ollama

检查：

`ollama --version`

运行：

`ollama run qwen3:4b`

### 3. CUDA PyTorch

项目图片生成需要支持 CUDA 的 PyTorch。

检查：

`torch.cuda.is_available()`

应返回：

`True`

### 4. 图片生成依赖

安装：

`py -m pip install diffusers transformers accelerate safetensors pillow`

### 5. TTS 依赖

安装：

`py -m pip install edge-tts mutagen`

### 6. Hugging Face Xet

如果模型下载出现 CAS / File Reconstruction 错误，可以设置：

`$env:HF_HUB_DISABLE_XET="1"`

### 7. 启动应用

运行：

`py -m streamlit run app.py`

浏览器访问：

`http://localhost:8501`

---

## 📂 Outputs

生成文件统一保存在：

`outputs/`

结构：

outputs/

├── images/

├── audio/

└── subtitles/

图片：

`outputs/images/scene_X_*.png`

音频：

`outputs/audio/scene_X.mp3`

字幕：

`outputs/subtitles/video.srt`

`outputs/` 已加入 `.gitignore`。

因此生成的大量媒体素材不会默认提交到 GitHub。

---

## 🎬 使用流程

输入主题

↓

选择视频风格

↓

选择视频时长

↓

点击：

`✨ 生成视频方案`

↓

获得：

- Title
- Hook
- Script
- 6 Scenes
- Image Prompt
- Video Prompt

↓

点击：

`🚀 一键生成全部分镜图片`

↓

获得 6 张 PNG

↓

点击：

`🔊 一键生成全部配音与字幕`

↓

获得：

- 6 段 MP3
- 1 个 SRT

↓

页面：

- 查看图片
- 播放配音
- 查看字幕
- 下载素材
- 导出 JSON / Script / Storyboard

---

## 🎯 项目目标

AI Short Video Studio 希望实现完整的 AI 短视频自动化 Workflow：

Topic

↓

LLM

↓

Title / Hook / Script

↓

Storyboard

↓

Image Prompt / Video Prompt

↓

AI Images

↓

TTS

↓

Subtitle

↓

Video Composition

↓

MP4

↓

Publishable Short Video

项目用于实践：

- Vibe Coding
- LLM Application Development
- Local LLM
- Local AI Image Generation
- GPU / CUDA
- Prompt Engineering
- Structured Output
- AI Workflow
- TTS
- Subtitle Automation
- Web App Development
- Multimedia Processing
- Git / GitHub

---

## 🗺 Roadmap

### ✅ 已完成

- [x] V0.1 Streamlit Prototype
- [x] V0.2 Local LLM
- [x] V0.3 Structured JSON
- [x] V0.4 Image / Video Prompt
- [x] V0.5 Export
- [x] V0.6 Local AI Image Generation
- [x] V0.7 Streamlit Image Generation
- [x] V0.8 Batch Image Generation
- [x] V0.9 TTS + Subtitle

### 🔜 V1.0 — Video Composition

- [ ] 安装并接入 FFmpeg
- [ ] 根据真实音频时长控制每张图片展示时间
- [ ] 合并 6 个 Scene
- [ ] 合并 6 段配音
- [ ] 加入 SRT 字幕
- [ ] 输出 MP4
- [ ] Streamlit 页面播放最终视频
- [ ] Streamlit 下载最终视频
- [ ] Topic → Video 完整 Workflow 跑通

### 🔮 V1.x — Engineering Upgrade

V1.0 完成后计划调研成熟 GitHub 开源项目，并对当前项目进行系统性升级。

重点研究：

- 项目目录分层
- Service / Model / UI 解耦
- 配置管理
- 模型缓存
- 日志系统
- 异常处理
- Pipeline Architecture
- Task Management
- Media Management
- Tests
- Requirements
- Docker
- Deployment
- Streamlit State Management
- FFmpeg 封装方式

升级原则：

> 先独立完成可工作的 MVP，再参考成熟工程实现进行 Benchmark 和重构。

---

## 🔐 安全说明

以下内容已加入 `.gitignore`：

- `.env`
- `outputs/`

不要上传：

- API Key
- Token
- Password
- Cookie
- 其他敏感凭据

文本模型主要运行在本机 Ollama。

图片模型运行在本机 NVIDIA GPU。

Edge TTS 需要联网请求语音服务。

---

## 📌 当前版本

**V0.9**

当前状态：

> ✅ Topic → Script → Storyboard → Image Prompt → 6 Images → 6 Voice Audios → SRT Subtitle 已完整跑通。

当前核心链路：

> ✅ Ollama + Qwen3 4B + Stable Diffusion 1.5 + PyTorch + CUDA + Edge TTS + SRT

下一步：

> 🎬 V1.0：使用 FFmpeg 将图片、配音和字幕真正合成为第一个 MP4 视频。