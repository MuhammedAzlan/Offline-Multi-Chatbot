# Offline AI Multi Tool Chatbot Starter

This is an upgraded starter project for a local/offline AI assistant.

## Features Included

- Offline chatbot using Ollama
- Browser-based UI
- PDF generator
- HTML page generator
- Text-to-voice module
- Simple text video generator
- Image generation integration placeholder
- Output file system

## Required Base Software

1. Python 3.10+
2. Ollama
3. Docker optional
4. FFmpeg recommended for video
5. Stable Diffusion WebUI or ComfyUI for real offline image generation

## Install

```bash
pip install -r requirements.txt
```

## Start Ollama

```bash
ollama pull llama3.1:8b
ollama serve
```

Or for lower-end PC:

```bash
ollama pull llama3.2:3b
```

## Run App

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

## About Photo Generation

This package includes the structure for image generation, but real offline image generation needs a Stable Diffusion engine.

Recommended:

- ComfyUI
- AUTOMATIC1111 Stable Diffusion WebUI
- Fooocus

Minimum GPU for decent offline image generation:

- NVIDIA GPU with 8GB VRAM
- Better: 12GB to 16GB VRAM

## About Video Generation

Included video module creates simple text-based MP4 videos.

For advanced AI video generation, offline setup requires very strong GPU and tools like:

- Stable Video Diffusion
- ComfyUI video workflows
- AnimateDiff
- Wan / Hunyuan video models, depending on system support

Most advanced AI video generation is heavy and not truly easy/free on low-end systems.

## Suggested Advanced Build

For production-level system:

- Frontend: Next.js or React
- Backend: FastAPI
- Local LLM: Ollama or vLLM
- Image: ComfyUI API
- Voice: Piper / Coqui / XTTS
- PDF: ReportLab / WeasyPrint
- Video: MoviePy + FFmpeg + ComfyUI video workflow
- Database: PostgreSQL
- Vector DB: Qdrant
- Login: JWT / OAuth
- Admin panel
