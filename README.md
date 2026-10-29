# The Ghost of Lord's 🏏👻
### *An Offline MCC Cricket Law Adjudicator & Arbiter of 1788, Powered by Google Gemma 2*

> Built for the **Hacktoberfest Open-Source AI Challenge Week 4: Ghost in the Machine** 🎃⚖️  
> Category target: **Best Use of Gemma** ($200) & Overall Prize

---

## 🏛️ What is "The Ghost of Lord's"?

Cricket has 42 official Laws governed exclusively by the Marylebone Cricket Club (MCC) at Lord's since 1788. Every year, matches are disrupted by fierce arguments over controversial dismissals:
- Was Jonny Bairstow's Ashes walkout fair game or against the Spirit of Cricket?
- Should Angelo Mathews have been given Timed Out when his helmet strap snapped?
- Is running out the non-striker ("Mankad") a legitimate run out or unfair play?

**The Ghost of Lord's** is an offline, privacy-first AI oracle possessed by the ancestral 1788 Victorian custodians of Lord's. It watches actual match footage, parses the complete 42 MCC Laws (2019 code) alongside the 1788 founding rules, and delivers a dual verdict:
1. 📜 **The Strict Official MCC Ruling:** Exact law citations, penalties, and out/not-out determinations.
2. 👻 **The Ghost's "Spirit of Cricket" Verdict:** Victorian gentleman commentary evaluating whether the action honors the chivalry and etiquette of the gentleman's game.

---

## 🔮 Why Open Innovation & Gemma 2 Matter

1. **Zero Cloud Dependency / 100% Offline:** Grassroots cricket grounds and club pavilions frequently lack Wi-Fi or cellular service. The Ghost of Lord's runs entirely locally on edge hardware via Google's open-weight **Gemma 2** (`gemma2:2b`) using Ollama.
2. **Deterministic Law Retrieval (Local RAG):** Instead of relying on closed-source cloud models that hallucinate rule numbers, the app locally indexes 4,300+ lines of the official MCC 2019 Laws and 1788 founding codes.
3. **Data Sovereignty & Open Weights:** Umpires, coaches, and clubs can audit and verify the model weights without vendor lock-in or recurring API subscription costs.

---

## ✨ Features

- ⚖️ **Full 42 MCC Laws Search:** In-memory keyword and token indexing across every official law clause.
- 📺 **Interactive Match Video Evidence:** Built-in YouTube match footage for iconic controversies (Angelo Mathews, Bairstow, Ashwin, Ben Stokes).
- 👻 **Dual-Perspective Judgments:** Reconciles the black-letter law against the historical Preamble ("The Spirit of Cricket").
- ⚡ **Interactive Streamlit Web Dashboard & CLI:** Fast token streaming, vintage Long Room aesthetic, and custom query mode.

---

## 🚀 Quickstart

### Prerequisites
1. Install [Ollama](https://ollama.com/) and pull Google's Gemma 2 model:
   ```bash
   ollama pull gemma2:2b
   ```
2. Python 3.9+ installed.

### Installation
```bash
git clone https://github.com/your-username/ghost-of-lords.git
cd ghost-of-lords
pip install -r requirements.txt
```

### Launch Streamlit Web UI
```bash
python -m streamlit run app.py
```

### Launch Interactive Terminal CLI
```bash
python -m mcc_oracle
```

---

## 📜 License
MIT License. Built with open-source AI for Hacktoberfest 2026.
