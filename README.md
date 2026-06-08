# <img src="./header.svg" width="100%" alt="wizhill05 console banner" />

```bash
$ whoami
Aryan Singh (Wizhill05)

$ locate --current
Faridabad, India [UTC +5:30]

$ cat bio.txt
"who even reads my github bio anyways"
```

---

## 🔮 Active Subroutines

Here are the custom engines, visualizers, and neural pipelines I build to bend browsers, bypass Cloudflare, and hack operating systems.

### 🧠 Agentic AI & Local LLM Pipelines
*   **[Resumer](https://github.com/Wizhill05/Resumer)**
    *   *Stealth Scraping + Multi-Agent Resume Optimization*
    *   A local-first backend that bypasses Cloudflare bot-detection to scrape job listings (LinkedIn/Indeed) via stealthy sessions, extracts technical requirements via Mistral AI NLP, and tailors ATS-optimized single-page PDF resumes using a CrewAI multi-agent orchestration team.
*   **[BioMetric](https://github.com/Wizhill05/bio-metric)**
    *   *AI-Powered Science Search Engine*
    *   An AI search engine that eliminates LLM hallucinations by enforcing strict synthesis from PubMed/Google Scholar databases. Powered by FastAPI, CrewAI agents, and a React frontend featuring a high-contrast neo-brutalist theme and custom 8-bit SVG pixel art icons.
*   **[LaunchYourLLM](https://github.com/Wizhill05/LaunchYourLLM)**
    *   *Local LLM Token Rate-Limiter & DBMS*
    *   A Next.js-based chat app and token-management DBMS designed to track token usage and enforce model-specific credit limits on locally running models (Phi-4, Gemma 3, DeepSeek R1).

### 📐 Applied Mathematics, Parallel GPU & Graphics
*   **[Z-Scroll](https://github.com/Wizhill05/z-scroll)**
    *   *3D Scrolling via Pure Mathematics*
    *   A React/Next.js/GSAP scroll interface that simulates 3D movement through depth (Z-axis) using pure mathematical transformations (exponential scaling, power parallax) on 2D elements. No WebGL, no Three.js. Just math.
*   **[GraXY](https://github.com/Wizhill05/Graxy)**
    *   *Real-time GPU Math Plane Renderer*
    *   A GPU-accelerated mathematical function visualizer built using CUDA and C++. Renders formulas per-pixel in parallel kernels, using OpenGL Pixel Buffer Objects (PBO) for zero-copy texture transfers to achieve VSync-refresh rates.
*   **[Spectofind](https://github.com/Wizhill05/Spectofind)**
    *   *Sound Classification Computer Vision Engine*
    *   Converts live audio input into Mel-spectrogram PNGs via `librosa`, feeding them into an ImageNet-pretrained `EfficientNet-B0` model for classification, connected to a websocket-based brutalist dashboard.

### 👾 Desktop Chaos & "Why Tho" Experiments
*   **[Flappy Window](https://github.com/Wizhill05/flappy-window)**
    *   *OS Window-Manager Game Hack*
    *   A Flappy Bird clone where the bird and the pipes are actual desktop OS windows spawned and moved dynamically. (Warning: turns system volume to 100 on death).
*   **[LyricBar](https://github.com/Wizhill05/LyricBar)**
    *   *Spotify Taskbar Overlay*
    *   A Python utility that overlays live-scraped Spotify lyrics directly onto the Windows taskbar.

---

## 🛠️ Tech Stack & Kernel Modules

```text
┌─────────────────────────────────────────────────────────────┐
│ LANGS:   Python 🐍 │ C++ ⚙️ │ TypeScript ⚙️ │ CUDA ⚡ │ Dart 🎯 │
├─────────────────────────────────────────────────────────────┤
│ AGENTS:  CrewAI 🤖 │ LangChain │ LiteLLM │ Mistral │ Gemini │
├─────────────────────────────────────────────────────────────┤
│ WEBS:    Next.js 15 │ React 19 │ Tailwind │ GSAP 🌀 │ GraphQL│
├─────────────────────────────────────────────────────────────┤
│ BACKS:   FastAPI │ Supabase │ SQLite │ MySQL │ Playwright   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧬 Architectural Equations

The math driving some of my active repositories:

### 1. Depth Perspective Scaling (used in `Z-Scroll`)
$$S(z) = e^{\text{scroll} - z}$$
*Computes the exponential scale of a element based on its depth plane $z$ and scroll camera position.*

### 2. Power Parallax Offset (used in `Z-Scroll`)
$$\text{Offset}(x, z) = \frac{6^{\text{scroll} - z} \cdot x}{2}\%$$
*Uses base-6 scaling to generate dramatic lateral displacement as elements fly past the camera.*

### 3. GPU Plane Mapping (used in `GraXY`)
$$f(x, y) = |x^2 - y^3| \implies \text{Color}(r, g, b)$$
*Evaluates functions in parallel CUDA threads to assign pixel color values in real-time.*

---

## 🔌 Network Sockets

```bash
$ netstat -an | grep wizhill
```
*   **Port 1337 (LinkedIn):** [in/justaryansingh](https://www.linkedin.com/in/justaryansingh)
*   **Port 8080 (Instagram):** [@just_aryansingh](https://instagram.com/just_aryansingh)
*   **Domain (Personal Space):** [aryansingh.space](https://aryansingh.space) *(currently parked)*

---
<div align="center">
  <img src="https://raw.githubusercontent.com/Wizhill05/Wizhill05/main/header.svg" width="0" height="0" alt="Preload" />
  <sub>⚡ Compiled and served from the local core.</sub>
</div>
