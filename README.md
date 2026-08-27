# 🎬 AI Short Video Studio

一个基于 **Python + Streamlit + Ollama + Stable Diffusion** 的 AI 短视频创作工具。

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
- 使用本地 Stable Diffusion 生成真实图片
- 在 Streamlit 页面中直接生成并展示分镜图片
- 一键批量生成全部 6 张分镜图片
- 单独重新生成某个镜头图片
- 下载单张分镜图片

当前文本生成使用：

`Ollama + Qwen3 4B`

当前图片生成使用：

`Stable Diffusion 1.5 + PyTorch + CUDA + NVIDIA GPU`

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

### ✅ V0.6 — Local AI Image Generation

- [x] 安装 CUDA 版本 PyTorch
- [x] Python 成功调用 NVIDIA GPU
- [x] 接入 Hugging Face Diffusers
- [x] 接入 Stable Diffusion 1.5
- [x] 使用 Image Prompt 生成真实图片
- [x] 图片自动保存到 outputs/images
- [x] 单分镜图片生成测试成功
- [x] 本地 GPU 生图 Workflow 跑通

### ✅ V0.7 — Streamlit Image Generation

- [x] image_service 接入 Streamlit
- [x] 每个分镜提供生成图片按钮
- [x] 使用对应 Image Prompt 生成图片
- [x] Streamlit 页面直接展示生成图片
- [x] 保存生成图片路径
- [x] 单张图片支持下载
- [x] generated_images 写入导出 JSON
- [x] 分镜到图片的 Web Workflow 跑通

### ✅ V0.8 — Batch Image Generation

- [x] 一键生成全部 6 个分镜图片
- [x] 自动读取每个 Scene 的 Image Prompt
- [x] 按顺序调用 Stable Diffusion 生图
- [x] 使用同一个本地 Pipeline 连续生成图片
- [x] 自动跳过已经生成的分镜
- [x] 显示批量生成进度
- [x] 自动保存图片路径
- [x] Streamlit 展示全部分镜图片
- [x] 支持单个镜头重新生成
- [x] 六分镜批量图片 Workflow 跑通

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

↓

一键生成全部分镜图片

↓

Scene 1 → Stable Diffusion → PNG

↓

Scene 2 → Stable Diffusion → PNG

↓

Scene 3 → Stable Diffusion → PNG

↓

Scene 4 → Stable Diffusion → PNG

↓

Scene 5 → Stable Diffusion → PNG

↓

Scene 6 → Stable Diffusion → PNG

↓

六张完整分镜视觉素材

---

## 🤖 本地 AI 模型

### 文本生成

当前模型：

`qwen3:4b`

运行方式：

`Ollama`

Ollama 默认 Local API：

`http://127.0.0.1:11434`

主要用于生成：

- Title
- Hook
- Script
- Storyboard
- Image Prompt
- Video Prompt

### 图片生成

当前模型：

`runwayml/stable-diffusion-v1-5`

运行框架：

- PyTorch
- Diffusers
- Transformers
- Accelerate
- CUDA

当前测试设备：

`NVIDIA GeForce RTX 3060 Laptop GPU`

显存：

`6 GB VRAM`

当前图片尺寸：

`512 × 512`

当前默认推理参数：

- Inference Steps：25
- Guidance Scale：7.5

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

Metadata 包含：

- `topic`
- `style`
- `duration`

生成图片后还会记录：

- `generated_images`

例如：

`generated_images["1"]`

表示镜头 1 当前生成图片的本地路径。

这些结构化数据将作为后续：

- AI 图片生成
- AI 视频生成
- TTS 配音
- 自动字幕
- 视频合成

模块的输入。

---

## 📤 当前导出能力

项目当前支持三种文本 / 数据导出格式。

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
- Generated Images

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

## 🖼️ 图片生成

图片生成逻辑位于：

`image_service.py`

主要流程：

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

默认输出目录：

`outputs/images/`

生成文件示例：

`scene_1_20260827_142124.png`

当前已经支持：

- Python 独立测试生成图片
- Streamlit 页面单分镜生成图片
- Streamlit 页面展示生成图片
- 下载单张生成图片
- 一键生成全部 6 张分镜图片
- 跳过已经生成的图片
- 单独重新生成某个镜头
- 保存所有生成图片路径到 Session State

---

## 🚀 批量图片生成

V0.8 增加了：

`🚀 一键生成全部分镜图片`

点击后程序会顺序处理：

Scene 1

↓

Scene 2

↓

Scene 3

↓

Scene 4

↓

Scene 5

↓

Scene 6

每个 Scene 都会读取对应的：

`scene["image_prompt"]`

然后调用本地 Stable Diffusion。

生成成功后图片会自动保存到：

`outputs/images/`

批量生成过程中会显示：

- 当前正在生成的镜头
- 总体生成进度
- 当前已生成图片数量
- 失败镜头错误信息

如果某个镜头已经存在图片，则批量生成时会自动跳过。

---

## 🌐 Streamlit 图片生成

用户生成短视频方案后，每个分镜都会出现图片生成按钮。

没有图片时：

`🖼️ 生成镜头 X 图片`

已经有图片时：

`🔄 重新生成镜头 X 图片`

点击后：

1. 读取当前 Scene 的 `image_prompt`
2. 调用 `image_service.py`
3. 加载 Stable Diffusion 1.5
4. 使用 RTX 3060 GPU 推理
5. 保存 PNG 图片
6. 返回图片路径
7. Streamlit 展示图片
8. 提供下载按钮

同时页面还提供：

`🚀 一键生成全部分镜图片`

用于批量处理全部 6 个分镜。

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
- Git
- GitHub

后续计划使用：

- TTS
- Subtitle
- FFmpeg
- AI Video Generation
- AI Workflow
- Public Deployment

---

## 📁 项目结构

AI-Short-Video-Studio/

├── app.py
├── ollama_service.py
├── image_service.py
├── test_ollama.py
├── test_api.py
├── test_image.py
├── README.md
├── .gitignore
├── .env
└── outputs/
    └── images/

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
- 调用本地图片生成服务
- 单独生成分镜图片
- 批量生成全部分镜图片
- 展示生成图片
- 下载生成图片
- 保存生成图片路径

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

### image_service.py

本地图片生成模块。

负责：

Image Prompt

↓

Stable Diffusion 1.5

↓

PyTorch + CUDA

↓

NVIDIA GPU

↓

PNG Image

图片默认保存到：

`outputs/images/`

### test_ollama.py

用于测试：

`Python → Ollama API → Qwen3`

是否可以正常连接。

### test_image.py

用于测试：

`Python → Stable Diffusion → CUDA → NVIDIA GPU → PNG`

是否可以正常生成真实图片。

### test_api.py

用于测试云端 LLM API。

当前项目主要使用本地 Ollama，因此文本生成不依赖云端 LLM API 额度。

---

## 🚀 本地运行

### 1. 安装基础依赖

运行：

`py -m pip install streamlit requests`

### 2. 安装 Ollama

安装完成后检查：

`ollama --version`

### 3. 下载并运行本地文本模型

当前使用：

`ollama run qwen3:4b`

### 4. 安装 CUDA 版本 PyTorch

项目图片生成需要支持 CUDA 的 PyTorch。

安装完成后可以使用：

`torch.cuda.is_available()`

如果返回：

`True`

即表示 CUDA 可以正常使用。

### 5. 安装图片生成依赖

需要安装：

- diffusers
- transformers
- accelerate
- safetensors
- pillow

例如：

`py -m pip install diffusers transformers accelerate safetensors pillow`

### 6. 测试 CUDA

可以检查：

`torch.cuda.get_device_name(0)`

当前测试结果：

`NVIDIA GeForce RTX 3060 Laptop GPU`

### 7. 测试图片生成

运行：

`py test_image.py`

成功后会在：

`outputs/images/`

生成 PNG 图片。

### 8. 启动 Streamlit

当前 PowerShell 会话可以先设置：

`$env:HF_HUB_DISABLE_XET="1"`

然后运行：

`py -m streamlit run app.py`

浏览器访问：

`http://localhost:8501`

---

## ⚠️ Hugging Face 下载说明

Stable Diffusion 模型首次运行时需要从 Hugging Face 下载模型文件。

首次下载文件较大，属于正常情况。

模型下载完成后会缓存在本机，后续运行通常无需重新完整下载。

如果 Hugging Face Xet 下载出现：

- CAS Client Error
- File Reconstruction Error
- error decoding response body

可以在当前 PowerShell 会话设置：

`$env:HF_HUB_DISABLE_XET="1"`

然后重新运行：

`py test_image.py`

或：

`py -m streamlit run app.py`

---

## 📂 输出文件说明

AI 图片默认保存到：

`outputs/images/`

例如：

`outputs/images/scene_1_20260827_142124.png`

`outputs/` 已加入 `.gitignore`。

因此生成的大量图片不会默认上传到 GitHub。

这样可以避免：

- Git 仓库体积快速变大
- 上传大量测试图片
- 提交不必要的生成文件

---

## 🎬 使用示例

输入主题：

> 一只猫发现家里的镜子通往另一个世界

选择：

- 视频风格：奇幻
- 视频时长：30 秒

系统生成：

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

点击：

`🚀 一键生成全部分镜图片`

↓

Stable Diffusion 1.5

↓

RTX 3060 GPU

↓

生成 6 张真实分镜图片

↓

网页展示全部图片

↓

单张图片下载

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
- Local LLM
- Local AI Image Generation
- GPU / CUDA
- API 调用
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
- [x] V0.6 Local AI Image Generation
- [x] V0.7 Streamlit Image Generation
- [x] V0.8 Batch Image Generation

### 🔜 V0.9 — TTS + Subtitle

- [ ] Voiceover 转语音
- [ ] 保存音频文件
- [ ] Streamlit 播放音频
- [ ] 自动生成字幕文件
- [ ] 输出 SRT
- [ ] 为最终视频合成准备音频和字幕素材

### 🔜 V1.0 — Video Composition

- [ ] 接入 FFmpeg
- [ ] 图片 + 音频 + 字幕合成
- [ ] 输出 MP4
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

### 🔮 后续计划

- [ ] AI Video Generation
- [ ] 使用 Video Prompt 生成动态镜头
- [ ] 内容模板系统
- [ ] 批量短视频生产
- [ ] 公网部署
- [ ] 更好的图片模型
- [ ] Prompt 优化
- [ ] 更丰富的视频风格
- [ ] 一键生成完整短视频

---

## 🔐 安全说明

`.env` 已加入 `.gitignore`。

`outputs/` 已加入 `.gitignore`。

请不要将以下内容上传到 GitHub：

- API Key
- Token
- 密码
- Cookie
- 其他敏感凭据

当前文本 LLM 服务运行在本机：

`127.0.0.1:11434`

图片生成同样在本机 NVIDIA GPU 上执行。

---

## 📌 当前版本

**V0.8**

当前状态：

> ✅ Streamlit + Ollama + Qwen3 4B + JSON Structured Output + Export + Stable Diffusion 1.5 + PyTorch + CUDA + 六分镜批量图片生成已跑通。

目前已经完成：

> 主题 → 标题 → Hook → 脚本 → 六分镜 → Image Prompt / Video Prompt → 六张 AI 分镜图片 → 导出

下一步：

> 🔊 接入 TTS，让短视频旁白真正生成音频，并为字幕和最终视频合成准备素材。