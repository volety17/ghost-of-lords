# NecroShell 👻💀
### *The Ghost in the Machine: An Offline Haunted Terminal Possessed by Gemma*

> Built for the **Hacktoberfest Open-Source AI Challenge Week 4: Ghost in the Machine** 🎃🕯️

NecroShell is an interactive POSIX/PowerShell terminal shell possessed by a supernatural spirit powered locally by Google's open-weight **Gemma 2** (or fallback local models like Qwen) running entirely offline via **Ollama**.

Whenever you enter shell commands, browse files, execute scripts, or trigger syntax errors, the Ghost watches from the machine, muttering eerie, atmospheric, and darkly humorous commentary, while subtly glitching the terminal.

---

## ✨ Features

- 🕯️ **Interactive Haunted REPL**: Real shell execution (PowerShell / CMD / Bash) with ghostly intercepts and live streaming whispers from the void.
- 🔮 **Zero Cloud / Pure Local Inference**: Powered by local open-weight **Gemma 2** (`gemma2:2b`) running via Ollama. 100% offline, private, and works even when the internet is cut!
- 🪦 **Día de los Muertos & Halloween Persona Modes**:
  - `spectre` - Malevolent Victorian machine spirit trapped in the silicon.
  - `ofrenda` - A warm, ancestral spirit remembering forgotten bytes and honoring the past.
  - `cyber_revenant` - Glitchy corrupted digital ghost haunting your system memory.
- ⚡ **Terminal Poltergeist FX**: Flickering typewriter text effects, spectral ASCII art, eerie sounds (cross-platform bells & frequencies), and possessed command translations.
- 📜 **Séance Mode (`seance <query>`)**: Conduct an offline séance to commune with forgotten code, dead languages (COBOL, ALGOL, Ada), or long-lost memories.
- 🎛️ **Possessed Commands**:
  - `necro-manifest` - Summon the spectral avatar of the machine.
  - `ofrenda` - Offer an offering (CPU cycles, memory, words of remembrance) to calm the spirit.
  - `exorcise` - Temporarily purge the spirit before it creeps back in.

---

## 🚀 Quickstart

### Prerequisites
1. [Ollama](https://ollama.com/) installed and running.
2. Pull Google's Gemma 2 model:
   ```bash
   ollama pull gemma2:2b
   ```
3. Python 3.9+ installed.

### Installation
```bash
git clone https://github.com/your-username/necro-shell.git
cd necro-shell
pip install -r requirements.txt
```

### Launch
```bash
python -m necro_shell
```
Or specify persona:
```bash
python -m necro_shell --persona ofrenda
```
