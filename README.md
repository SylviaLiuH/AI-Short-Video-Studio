# 🎬 AI Short Video Studio

一个基于 **Python + Streamlit + Ollama + Stable Diffusion + Edge TTS + FFmpeg** 的 AI 短视频自动生成工具。

用户输入一个简单主题，并选择视频风格和时长，系统可以自动完成：

- 短视频标题生成
- 前 3 秒 Hook 生成
- 完整脚本生成
- 6 个结构化分镜生成
- Image Prompt 生成
- Video Prompt 生成
- 本地 AI 分镜图片生成
- 6 个分镜批量生图
- AI 中文配音
- SRT 字幕生成
- 图片 / 配音 / 字幕自动合成
- 最终 MP4 视频输出
- Streamlit 页面预览
- JSON / Script / Storyboard / Image / Audio / Subtitle / Video 下载

当前已经跑通完整 Workflow：

`Topic → Script → Storyboard → Images → Voice → Subtitle → MP4`

---

# ✨ V1.0 功能总览

当前 V1.0 已经实现：

- [x] 用户输入视频主题
- [x] 视频风格选择
- [x] 视频时长选择
- [x] 本地 LLM 文案生成
- [x] JSON Structured Output
- [x] 6 个结构化分镜
- [x] Image Prompt
- [x] Video Prompt
- [x] JSON 导出
- [x] Script 导出
- [x] Storyboard 导出
- [x] Stable Diffusion 本地生图
- [x] CUDA GPU 推理
- [x] 单分镜图片生成
- [x] 六分镜批量图片生成
- [x] 图片下载
- [x] Edge TTS 配音
- [x] 六分镜批量配音
- [x] 音频播放
- [x] 音频下载
- [x] 自动读取音频真实时长
- [x] 自动生成 SRT 字幕
- [x] SRT 下载
- [x] FFmpeg 视频合成
- [x] 图片 + 配音 + 字幕合成
- [x] 输出 MP4
- [x] Streamlit 播放最终视频
- [x] 最终 MP4 下载
- [x] Topic → Video 完整 Workflow

---

# 🧠 AI Workflow

完整流程：

用户输入：

Topic / Style / Duration

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

Title

↓

Hook

↓

Script

↓

6 Scenes

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

FFmpeg

↓

图片 + 音频 + 字幕

↓

720 × 1280 MP4

↓

Streamlit 页面预览

↓

最终视频下载

---

# 🚀 版本记录

## ✅ V0.1 — Streamlit Prototype

完成基础 Web 页面原型。

- [x] Topic 输入
- [x] Style 选择
- [x] Duration 选择
- [x] Mock Title
- [x] Mock Hook
- [x] Mock Script
- [x] Mock Storyboard

---

## ✅ V0.2 — Local LLM

将静态 Mock 内容替换为真实 AI 生成。

- [x] 安装 Ollama
- [x] 本地运行 Qwen3 4B
- [x] Python 调用 Ollama Local API
- [x] Streamlit 调用本地模型
- [x] 根据用户输入动态生成短视频方案

Workflow：

`Streamlit → Python → Ollama → Qwen3`

---

## ✅ V0.3 — Structured JSON

将 LLM 自由文本输出改造成结构化数据。

- [x] JSON Structured Output
- [x] 关闭 Qwen3 Thinking
- [x] 固定输出合法 JSON
- [x] Title 独立字段
- [x] Hook 独立字段
- [x] Script 独立字段
- [x] Scenes 独立字段
- [x] 固定生成 6 个分镜
- [x] Visual 独立字段
- [x] Voiceover 独立字段
- [x] Sound / BGM 独立字段

---

## ✅ V0.4 — Image Prompt / Video Prompt

为每个分镜增加 AI 视觉生成 Prompt。

每个 Scene 新增：

- [x] `image_prompt`
- [x] `video_prompt`

规则：

- 中文生成 Visual / Voiceover / Sound
- 英文生成 Image Prompt
- 英文生成 Video Prompt

用于后续：

- AI 图片生成
- AI 视频生成
- 自动化视觉 Workflow

---

## ✅ V0.5 — Export

增加生成结果导出能力。

支持：

- [x] 完整 JSON
- [x] Script TXT
- [x] Storyboard Markdown
- [x] Metadata
- [x] Topic
- [x] Style
- [x] Duration
- [x] Streamlit Download Button
- [x] Session State

---

## ✅ V0.6 — Local AI Image Generation

第一次实现真实 AI 图片生成。

使用：

- Stable Diffusion 1.5
- PyTorch
- CUDA
- Diffusers
- NVIDIA GPU

完成：

- [x] CUDA PyTorch 环境
- [x] GPU 检测
- [x] Stable Diffusion Pipeline
- [x] Image Prompt → PNG
- [x] 自动保存图片
- [x] 单分镜生图测试

Workflow：

`Image Prompt → Stable Diffusion → CUDA → PNG`

---

## ✅ V0.7 — Streamlit Image Generation

将图片生成能力接入 Web 页面。

- [x] 每个 Scene 增加图片生成按钮
- [x] Streamlit 调用 Stable Diffusion
- [x] 页面显示生成图片
- [x] 图片路径保存至 Session State
- [x] 图片下载
- [x] generated_images 写入 JSON

---

## ✅ V0.8 — Batch Image Generation

实现完整 Storyboard 批量图片生成。

- [x] 一键生成 6 张分镜图片
- [x] 自动读取每个 Image Prompt
- [x] 顺序执行 GPU 推理
- [x] 自动跳过已有图片
- [x] 显示生成进度
- [x] 保存全部图片路径
- [x] 单个 Scene 支持重新生成
- [x] Streamlit 展示完整视觉 Storyboard

Workflow：

`6 Scenes → 6 Image Prompts → Stable Diffusion → 6 PNG`

---

## ✅ V0.9 — TTS + Subtitle

增加 AI 配音和字幕生成。

使用：

- Edge TTS
- Mutagen

完成：

- [x] Voiceover → MP3
- [x] 单镜头 TTS
- [x] 六分镜批量 TTS
- [x] 音频自动保存
- [x] 获取 MP3 真实时长
- [x] 自动计算字幕时间轴
- [x] 自动生成 SRT
- [x] Streamlit 一键配音
- [x] Streamlit 播放 MP3
- [x] MP3 下载
- [x] SRT 页面展示
- [x] SRT 下载

Workflow：

`Voiceover → Edge TTS → MP3 → Duration → SRT`

---

## ✅ V1.0 — Video Composition

第一次实现完整 AI 短视频输出。

使用：

`FFmpeg`

完成：

- [x] FFmpeg 环境
- [x] 单 Scene 视频生成
- [x] 根据真实配音时长控制 Scene 时长
- [x] 6 个 Scene 合并
- [x] 音频合并
- [x] SRT 字幕烧录
- [x] 输出 H.264 MP4
- [x] 720 × 1280 竖屏视频
- [x] Streamlit 一键生成最终视频
- [x] 页面直接预览 MP4
- [x] 最终视频下载
- [x] final_video_path 写入 JSON
- [x] Topic → Video 完整 Workflow 跑通

---

# 🤖 AI 模型

## 文本模型

当前使用：

`Qwen3 4B`

通过：

`Ollama`

运行。

默认 Ollama API：

`http://127.0.0.1:11434`

主要负责：

- Title
- Hook
- Script
- Storyboard
- Visual
- Voiceover
- Sound
- Image Prompt
- Video Prompt

---

## 图片模型

当前使用：

`runwayml/stable-diffusion-v1-5`

通过：

- PyTorch
- Diffusers
- CUDA

运行。

当前测试 GPU：

`NVIDIA GeForce RTX 3060 Laptop GPU`

显存：

`6 GB VRAM`

当前默认生成尺寸：

`512 × 512`

当前默认参数：

- Inference Steps：25
- Guidance Scale：7.5

---

# 🖼️ AI Image Generation

图片生成逻辑位于：

`image_service.py`

流程：

Image Prompt

↓

Stable Diffusion Pipeline

↓

PyTorch

↓

CUDA

↓

NVIDIA GPU

↓

PNG Image

默认保存目录：

`outputs/images/`

示例：

`outputs/images/scene_1_20260827_182103.png`

支持：

- 单 Scene 生图
- 批量 Scene 生图
- 图片重新生成
- 图片下载
- 页面展示
- 图片路径记录

---

# 🔊 AI TTS

TTS 逻辑位于：

`tts_service.py`

当前使用：

`Edge TTS`

默认中文声音：

`zh-CN-XiaoxiaoNeural`

流程：

Voiceover

↓

Edge TTS

↓

MP3

默认输出：

`outputs/audio/`

例如：

`outputs/audio/scene_1.mp3`

`outputs/audio/scene_2.mp3`

`outputs/audio/scene_3.mp3`

...

`outputs/audio/scene_6.mp3`

Edge TTS 需要网络连接。

---

# 💬 Subtitle

字幕由：

`tts_service.py`

自动生成。

程序使用 Mutagen 获取每段 MP3 的真实时长。

流程：

Scene 1 Duration

↓

Scene 2 Start Time

↓

Scene 2 Duration

↓

Scene 3 Start Time

↓

...

↓

完整 Timeline

↓

SRT

默认字幕：

`outputs/subtitles/video.srt`

示例：

1

00:00:00,000 --> 00:00:03,200

第一段旁白

2

00:00:03,200 --> 00:00:06,500

第二段旁白

---

# 🎬 Video Composition

视频合成逻辑位于：

`video_service.py`

使用：

`FFmpeg`

首先逐个创建 Scene 视频：

`scene_1.png + scene_1.mp3 → scene_1.mp4`

`scene_2.png + scene_2.mp3 → scene_2.mp4`

...

`scene_6.png + scene_6.mp3 → scene_6.mp4`

然后：

6 个 Scene MP4

↓

FFmpeg concat

↓

完整无字幕视频

↓

SRT

↓

Subtitle Burn-in

↓

Final MP4

默认视频规格：

- Width：720
- Height：1280
- FPS：30
- Codec：H.264
- Audio：AAC
- Pixel Format：yuv420p

最终视频：

`outputs/videos/final_video_*.mp4`

---

# 📦 数据结构

## Video Plan

包含：

- `title`
- `hook`
- `script`
- `scenes`

## Scene

每个 Scene 包含：

- `scene_number`
- `visual`
- `voiceover`
- `sound`
- `image_prompt`
- `video_prompt`

## Metadata

包含：

- `topic`
- `style`
- `duration`

## Generated Assets

运行后还会保存：

- `generated_images`
- `generated_audio`
- `subtitle_path`
- `final_video_path`

---

# 📤 导出功能

## JSON

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
- Final Video Path

---

## Script

文件：

`video_script.txt`

包含：

- Title
- Hook
- Script

---

## Storyboard

文件：

`storyboard.md`

包含：

- Title
- Hook
- Script
- Visual
- Voiceover
- Sound
- Image Prompt
- Video Prompt

---

## Images

格式：

`PNG`

支持 Streamlit 下载。

---

## Audio

格式：

`MP3`

支持：

- 页面播放
- 页面下载

---

## Subtitle

格式：

`SRT`

支持页面查看与下载。

---

## Final Video

格式：

`MP4`

支持：

- Streamlit 页面预览
- MP4 下载

---

# 📁 项目结构

AI-Short-Video-Studio/

├── app.py
├── ollama_service.py
├── image_service.py
├── tts_service.py
├── video_service.py
├── test_ollama.py
├── test_api.py
├── test_image.py
├── test_tts.py
├── test_tts_batch.py
├── test_video.py
├── README.md
├── .gitignore
├── .env
└── outputs/
    ├── images/
    ├── audio/
    ├── subtitles/
    └── videos/

---

# 🧩 文件说明

## app.py

Streamlit Web App 主入口。

负责：

- 用户输入
- 视频方案生成
- Session State
- Storyboard 展示
- 单分镜图片生成
- 批量图片生成
- TTS 配音
- SRT 字幕
- 视频合成
- 最终视频预览
- 文件下载
- JSON 导出

---

## ollama_service.py

本地 LLM Service。

流程：

`Python → Ollama → Qwen3 → Structured JSON`

---

## image_service.py

图片生成 Service。

流程：

`Image Prompt → Stable Diffusion → CUDA → PNG`

---

## tts_service.py

TTS 与 Subtitle Service。

流程：

`Voiceover → Edge TTS → MP3 → Duration → SRT`

---

## video_service.py

视频合成 Service。

流程：

`Images + Audio + SRT → FFmpeg → MP4`

---

## test_ollama.py

测试：

`Python → Ollama → Qwen3`

---

## test_image.py

测试：

`Python → Stable Diffusion → CUDA → PNG`

---

## test_tts.py

测试：

`Text → Edge TTS → MP3`

---

## test_tts_batch.py

测试：

`6 Voiceovers → 6 MP3 → SRT`

---

## test_video.py

测试：

`6 Images + 6 MP3 + SRT → FFmpeg → MP4`

---

## test_api.py

用于测试云端 LLM API。

当前核心 LLM Workflow 使用本地 Ollama。

---

# 🛠 技术栈

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
- FFmpeg
- Git
- GitHub

---

# 🚀 本地运行

## 1. Python

确认 Python：

`py --version`

---

## 2. 安装基础依赖

`py -m pip install streamlit requests`

---

## 3. 安装 Ollama

检查：

`ollama --version`

运行模型：

`ollama run qwen3:4b`

---

## 4. 安装 CUDA PyTorch

项目图片生成需要 CUDA 版本 PyTorch。

检查：

`torch.cuda.is_available()`

正常应返回：

`True`

当前测试 GPU：

`NVIDIA GeForce RTX 3060 Laptop GPU`

---

## 5. 安装图片生成依赖

`py -m pip install diffusers transformers accelerate safetensors pillow`

---

## 6. 安装 TTS 依赖

`py -m pip install edge-tts mutagen`

---

## 7. 安装 FFmpeg

Windows 可以使用：

`winget install Gyan.FFmpeg`

安装完成后重新打开终端。

检查：

`ffmpeg -version`

---

## 8. Hugging Face Xet

如果 Stable Diffusion 模型下载出现：

- CAS Client Error
- File Reconstruction Error
- error decoding response body

可以在当前 PowerShell 设置：

`$env:HF_HUB_DISABLE_XET="1"`

---

## 9. 启动 Streamlit

运行：

`py -m streamlit run app.py`

浏览器访问：

`http://localhost:8501`

---

# 🎮 使用方法

## Step 1

输入一个短视频主题。

例如：

> 一只猫发现家里的镜子通往另一个世界

---

## Step 2

选择：

- 视频风格
- 视频时长

---

## Step 3

点击：

`✨ 生成视频方案`

获得：

- Title
- Hook
- Script
- 6 Scenes
- Image Prompt
- Video Prompt

---

## Step 4

点击：

`🚀 一键生成全部分镜图片`

系统会使用本地 Stable Diffusion 生成 6 张 PNG。

---

## Step 5

点击：

`🔊 一键生成全部配音与字幕`

系统自动生成：

- 6 段 MP3
- 1 个 SRT

---

## Step 6

等待三个状态全部准备完成：

- 🖼️ 图片：已准备
- 🔊 配音：已准备
- 💬 字幕：已准备

---

## Step 7

点击：

`🎬 生成最终视频`

FFmpeg 会自动完成：

- Scene Video
- Audio
- Scene Concatenation
- Subtitle Burn-in
- MP4 Encoding

---

## Step 8

页面出现：

`🎉 成品预览`

可以：

- 播放最终视频
- 下载 MP4

---

# 📂 Outputs

所有生成素材统一放在：

`outputs/`

结构：

outputs/

├── images/

├── audio/

├── subtitles/

└── videos/

---

## Images

`outputs/images/`

---

## Audio

`outputs/audio/`

---

## Subtitle

`outputs/subtitles/video.srt`

---

## Video

`outputs/videos/final_video_*.mp4`

---

`outputs/` 已加入 `.gitignore`。

生成素材不会默认提交到 GitHub。

---

# ⚠️ 当前 V1.0 的限制

V1.0 的核心目标是：

> 跑通完整 AI 短视频自动化 Workflow。

因此当前生成质量仍然属于 MVP 阶段。

主要限制包括：

### 1. 图片一致性较弱

当前 6 个 Scene 分别独立使用 Stable Diffusion 1.5 生成。

因此可能出现：

- 人物外观变化
- 服装变化
- 场景风格变化
- 主体一致性不足

---

### 2. 视频目前主要是静态图片

当前视频本质是：

`Static Image + Voice + Subtitle`

所以视觉效果更接近：

- Storyboard Video
- Slideshow
- PPT-style Video

暂未实现：

- Image Animation
- Camera Motion
- AI Video Generation
- Scene Transition

---

### 3. TTS 表现有限

当前 Edge TTS 可以完成语音生成，但：

- 情绪表现有限
- 角色感有限
- 节奏可能不完全自然
- 不同内容缺少自动 Voice Selection

---

### 4. 视频节奏较基础

每个 Scene 的持续时间主要由对应 MP3 的真实时长决定。

暂未加入：

- Pause
- Transition
- Beat Sync
- BGM Mixing
- Sound Effects Mixing
- Dynamic Timing

---

### 5. 图片比例仍需优化

Stable Diffusion 当前默认生成：

`512 × 512`

最终视频为：

`720 × 1280`

因此目前通过：

`scale + pad`

转换成竖屏视频。

未来可以直接生成：

`9:16`

视觉素材。

---

# 🎯 项目目标

AI Short Video Studio 的目标不是单纯制作一个 Streamlit Demo。

项目希望探索：

> 如何将多个 AI / Multimedia 模块组合成一个完整的自动化内容生产 Pipeline。

最终方向：

Topic

↓

LLM

↓

Script

↓

Storyboard

↓

Image Generation

↓

Video Generation

↓

TTS

↓

Subtitle

↓

Audio / BGM

↓

Video Composition

↓

Publishable Short Video

---

# 💡 项目实践内容

本项目用于实践：

- Vibe Coding
- LLM Application Development
- Local LLM
- Structured Output
- Prompt Engineering
- Local AI Deployment
- Stable Diffusion
- GPU / CUDA
- AI Image Generation
- TTS
- Subtitle Automation
- FFmpeg
- Multimedia Processing
- Streamlit
- Session State
- Service Architecture
- AI Workflow
- Pipeline Design
- Git
- GitHub

---

# 🗺 Roadmap

## ✅ V1.0 — MVP Complete

当前已经完成：

- [x] Topic
- [x] Script
- [x] Storyboard
- [x] Image Prompt
- [x] Video Prompt
- [x] AI Images
- [x] AI Voice
- [x] Subtitle
- [x] Video Composition
- [x] MP4
- [x] Export
- [x] Streamlit Workflow

---

# 🔮 V1.x — Engineering Upgrade

V1.0 完成后，下一阶段将不再单纯堆新功能，而是开始进行：

> GitHub Open Source Benchmark + Engineering Refactor

计划搜索和研究成熟开源项目：

- AI Video Generator
- Text-to-Video Pipeline
- Stable Diffusion Web App
- AI Content Generator
- Multimedia Automation
- FFmpeg Pipeline
- TTS Workflow

重点研究：

- 项目目录结构
- UI / Service / Model 分层
- Pipeline Architecture
- 配置管理
- 模型缓存
- State Management
- Logging
- Exception Handling
- Task Queue
- Media Management
- File Management
- Requirements
- Tests
- Docker
- Deployment
- FFmpeg Wrapper
- GPU Resource Management

升级原则：

> 先完成自己的 MVP，再通过成熟开源项目 Benchmark 找到工程差距，并进行针对性重构。

---

# 🔮 V1.1 — 视觉质量升级

计划：

- [ ] 9:16 图片生成
- [ ] 更好的 Stable Diffusion 模型
- [ ] Prompt 优化
- [ ] Negative Prompt 优化
- [ ] Seed 控制
- [ ] Character Consistency
- [ ] Scene Consistency
- [ ] 图片质量参数设置

---

# 🔮 V1.2 — 视频动态化

计划：

- [ ] 图片缩放动画
- [ ] Pan / Zoom
- [ ] Scene Transition
- [ ] Ken Burns Effect
- [ ] Video Prompt 接入
- [ ] AI Video Generation
- [ ] 动态 Scene

---

# 🔮 V1.3 — Audio Upgrade

计划：

- [ ] Voice Selection
- [ ] 多种中文声音
- [ ] 不同角色声音
- [ ] Rate 调节
- [ ] Emotion / Style
- [ ] BGM
- [ ] Sound Effects
- [ ] Audio Mixing

---

# 🔮 V1.4 — Product Upgrade

计划：

- [ ] Generation History
- [ ] Project Management
- [ ] Template System
- [ ] Batch Content Generation
- [ ] Save / Load Project
- [ ] Retry Failed Task
- [ ] Progress Management
- [ ] Better Error Handling

---

# 🔮 V2.0 — Production Workflow

长期目标：

输入：

`Topic`

输出：

`Publishable Short Video`

进一步支持：

- 自动选题
- 自动脚本
- 自动视觉设计
- 自动素材生成
- 自动配音
- 自动音乐
- 自动字幕
- 自动视频生成
- 自动合成
- 批量生产

---

# 🔐 安全说明

以下内容已加入 `.gitignore`：

- `.env`
- `outputs/`

请不要上传：

- API Key
- Token
- Password
- Cookie
- Session
- 其他敏感凭据

文本模型主要通过 Ollama 在本地运行。

图片模型通过本地 NVIDIA GPU 运行。

Edge TTS 需要网络连接。

---

# 📌 当前版本

**V1.0**

当前状态：

> ✅ AI Short Video Studio V1.0 MVP 已完成。

已经跑通完整流程：

> **Topic → Script → Storyboard → Image Prompt → AI Images → Voice → Subtitle → FFmpeg → MP4**

当前版本虽然在图片一致性、配音质量、动态视觉和视频节奏方面仍然属于 MVP 阶段，但已经完成了完整可运行的 AI 短视频生产 Pipeline。

下一阶段：

> 🔍 GitHub Open Source Benchmark → 分析成熟 AI Video 项目 → Engineering Refactor → V1.x 质量升级。