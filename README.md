# 🎬 AI Short Video Studio

一个轻量级的 AI 短视频内容生成工具。

输入一个主题后，生成短视频标题、Hook、脚本和分镜方案，后续将逐步接入 LLM、AI 图片、配音和视频生成能力。

## ✨ 当前功能

### V0.1

目前支持：

- 输入短视频主题
- 选择视频风格
- 选择视频时长
- 生成视频标题
- 生成开场 Hook
- 生成短视频脚本
- 生成 6 个分镜

> 当前 V0.1 使用的是 Mock 数据，主要用于完成产品原型和页面流程。
>
> 下一版本将接入真实 LLM API，根据用户输入实时生成不同内容。

## 🛠 技术栈

- Python
- Streamlit
- Git / GitHub

## 🚀 本地运行

安装 Streamlit 后，在项目目录运行：

```bash
py -m streamlit run app.py
```

浏览器访问：

```text
http://localhost:8501
```

## 🗺 开发计划

- [x] V0.1 Streamlit 页面原型
- [ ] 接入 LLM API
- [ ] JSON 结构化输出
- [ ] AI 图片 Prompt 生成
- [ ] AI 图片生成
- [ ] TTS AI 配音
- [ ] 自动字幕生成
- [ ] 图片 / 音频 / 字幕视频合成
- [ ] 完整短视频生成 Workflow
- [ ] 公网部署

## 🎯 项目目标

希望通过这个项目探索一套完整的 AI 短视频生产流程：

主题输入

→ AI 生成 Hook 和脚本

→ 自动生成分镜

→ 生成图片 / 视频 Prompt

→ AI 图片或视频生成

→ AI 配音

→ 字幕

→ 自动合成短视频

最终将一个简单的创意，转化为可重复使用的 AI 内容生产 Workflow。

## 📌 当前版本

V0.1