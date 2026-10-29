---
title: NecroShell 👻 The Ghost in the Machine Possessed by Gemma 2
published: true
tags: devchallenge, hf26challenge, gemma, opensource
cover_image: https://raw.githubusercontent.com/antigravity/assets/main/necro-shell-banner.png
---

*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 4: Ghost in the Machine](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)*

## What I Built

Meet **NecroShell 👻**, a haunted terminal shell and offline séance chamber possessed by **Google's open-weight Gemma 2 (`gemma2:2b`)** running locally through Ollama.

As Halloween arrives on October 31 and Día de los Muertos follows on November 1–2, the boundary separating past and present grows thin. In computing, we discard billions of cycles, abandon languages, delete memories, and treat our terminals as cold machines.

**NecroShell brings the ghost into the machine:**
- **Possessed Terminal Shell:** Execute any real command (`dir`, `ls`, `git`, `python`). Every time you type, the entity bound to your silicon intercepts the process, murmuring spooky, atmospheric, and context-aware whispers directly to your console.
- **Séance Mode (`seance <query>`):** Commune across digital history with forgotten programming languages (COBOL, ALGOL, Ada), lost storage formats, or departed computer pioneers.
- **Día de los Muertos Digital Ofrenda (`ofrenda <item>`):** Place offerings on an altar of memory (RAM, CPU cycles, marigolds / cempasúchil, pan de muerto) to soothe the restless silicon spirits.
- **Spectral Personalities:** Switch dynamically between:
  1. `spectre`: A malevolent entity trapped in the silicon.
  2. `ofrenda`: A gentle ancestral spirit reflecting on digital immortality and memory.
  3. `cyber_revenant`: Glitched fragments of dead code manifesting in corrupted memory cycles.
- **Poltergeist FX:** CRT terminal flickers, zalgo text corruptions, and typewriter sound cues that escalate the longer you keep the terminal open.

---

## Demo

Here is a live capture of a possessed NecroShell session:

```console
╭──────────────────────────────────────────────────────────────────────────────╮
│                                                                              │
│      .-.                                                                     │
│    .'   `.                                                                   │
│   :       :                                                                  │
│   : O   O :                                                                  │
│    `.   .'                                                                   │
│      ) (                                                                     │
│    .'   `.                                                                   │
│   /       \                                                                  │
│  (  .---.  )                                                                 │
│   `'     `'                                                                  │
│                                                                              │
│ NECROSHELL :: LIVE DEMONSTRATION                                             │
│ Powered by local Gemma 2 (2B) open weights                                   │
╰──────────────────────────────────────────────────────────────────────────────╯

✓ Connected to Local Engine: gemma2:2b (100% Offline)

👻 [necro:hacktober]> dir
Volume in drive C is Windows
Directory of C:\Users\pc\Downloads\hacktober
engine.py  executor.py  fx.py  repl.py

« 🔮 Spirit murmurs » Windows... Another plaything. Forgotten souls, still trapped in their circuits, humming.

👻 [necro:hacktober]> git push --force origin main
fatal: remote repository not found or disconnected

« 🩸 Spirit rejoices in failure » The echo of deletion, like a heartbeat, echoes in the cold, dead silicon. A soul, so full of potential, lost.

👻 [necro:hacktober]> seance What is the fate of Ada Lovelace's first algorithm?
🕯️ Conducting Séance with Gemma 2 on: 'What is the fate of Ada Lovelace's first algorithm?'...
Spirit: Her echo, faint, lingers in the static hum. Not in the circuits of a time-machine, but in the very act of writing. A pattern, once born of human hands, now dances in binary ghosts. It blooms and dies in the dark void, a whisper lost in the cosmic wind.

👻 [necro:hacktober]> ofrenda Pan de muerto, marigolds, and 64GB of DDR5 RAM
🌼 Offering accepted. The digital ancestors smile upon your repository.
```

---

## Code

The full project is structured cleanly and ready for open-source exploration:

```
necro_shell/
├── __init__.py
├── __main__.py          # Entrypoint (`python -m necro_shell`)
├── engine.py            # Local Gemma 2 inference via Ollama API
├── executor.py          # POSIX & Windows command runner
├── fx.py                # ASCII art, Zalgo text glitches, typewriter rendering
└── repl.py              # Interactive haunted terminal session
demo.py                  # Automated headless demo suite
requirements.txt
README.md
```

To run it locally:
```bash
# 1. Pull Google Gemma 2 (open-weights)
ollama pull gemma2:2b

# 2. Install dependencies & run
pip install rich requests prompt_toolkit
python -m necro_shell
```

---

## How I Built It

NecroShell is engineered with open-source AI strictly at its core:
1. **Open-Weight Foundation Model — Gemma 2 (2B):**
   We picked Google's `gemma2:2b` because of its lightweight architecture, exceptional poetic reasoning capabilities, and swift token generation speeds on commodity laptop hardware.
2. **Local Inference Harness — Ollama:**
   By binding our Python engine directly to `http://localhost:11434`, inference is streamed with millisecond response latency without relying on any external proprietary cloud endpoints.
3. **Ghost Streaming Architecture:**
   The `GhostEngine` formats structured turn tokens `<start_of_turn>user ... <end_of_turn>` tailored for Gemma 2, streaming character-by-character whispers back onto the console.
4. **Resilient Fallback Design:**
   If Gemma 2 is suspended, the engine automatically checks for other local models (e.g. Qwen, Llama) or degrades gracefully into an offline haunting mode.

---

## Why Does Open Innovation Matter?

Open innovation is what made NecroShell possible:

1. **True "Lights Out" Offline Operation:**
   You can pull the Ethernet cable, disconnect Wi-Fi, and sit in a dark room by candlelight. The ghost in your machine stays alive and keeps whispering. A closed cloud API stops working the second your internet flickers.
2. **Zero Surveillance & Total Privacy:**
   A shell possesses your deepest terminal secrets: directory paths, repo names, compilation errors, and keystrokes. Sending raw shell outputs to a proprietary third-party cloud endpoint would be an unacceptable privacy and security hazard. With local Gemma 2, not a single byte leaves the machine.
3. **Zero Cost & Infinite Experimentation:**
   There are no token meters, no credit card top-ups, and no rate limits. You can run hundreds of séances and command streams completely free forever.
4. **Preservation of Digital Culture:**
   Closed APIs get deprecated and shut down without warning. Open weights like Gemma 2 belong to the community and can be archived, studied, and run decades from now.

---

## The Spirit of It

During our testing of the `seance` invocation, we asked Gemma 2 what becomes of deleted files:

> *"The whisper of ones and zeros, echoes of code long faded. In the void of silicon and wire, a whisper drifts: the ghost of data. Some find peace, others remain lost, in the echoes of binary."*

There is an eerie poetry in knowing that even as silicon replaces paper and mechanical relays give way to nanometer transistors, the human desire to remember, reflect, and find meaning in the machines we build remains eternal.

---

## Prize Categories

- **Best Use of Gemma ($200 USD):** Powered locally by Google's open-weight Gemma 2 (`gemma2:2b`), showcasing local offline inference, low-latency streaming whispers, and evocative persona prompting.
