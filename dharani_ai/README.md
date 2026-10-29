# DharaniAI (ధరణి / धरणी) 🌾☀️
### *Offline Climate Resilience, Micro-Weather Physics & Drought Advisory for Indian Drylands*

> Powered by **Google Gemma 2** running locally & 100% offline via **Ollama**.

---

## 🌍 The Problem
Over **68% of India's cultivable area is vulnerable to droughts**, with arid and semi-arid rain-shadow belts like **Rayalaseema (AP), Marathwada (MH), Bundelkhand (UP/MP), North Karnataka, and Western Rajasthan** facing devastating crop failures from heatwaves, shifting monsoons, and extreme evapotranspiration.

Smallholder farmers in these regions face two major challenges:
1. **Connectivity Deserts**: Cellular towers and power grids often drop during extreme weather and heatwaves, rendering cloud-dependent apps unusable.
2. **Generic Forecasts vs. Actionable Science**: Knowing tomorrow will be 41°C does not tell a farmer **how many liters of water their crop is losing** or **how to prevent flower drop**.

---

## 💡 The Solution: DharaniAI
**DharaniAI** brings state-of-the-art agro-meteorological science and official **ICAR & CRIDA (Central Research Institute for Dryland Agriculture)** contingency plans directly to the farm edge, running entirely offline on local open-weight **Gemma 2**.

### Key Modules:
- **☀️ Micro-Climate Physics Engine**: Implements the Tetens and FAO-56 Hargreaves equations to compute real-time **Vapor Pressure Deficit (VPD)** and **Reference Evapotranspiration ($ET_0$)** in liters/hectare/day.
- **🌾 Indian Dryland Agronomy RAG**: Pre-indexed database covering critical water sensitivity stages, emergency foliar anti-transpirant sprays (KNO3, Kaolin, Planofix), and regenerative soil practices (Jeevamrutha, biochar, mulching).
- **🚜 Precision Farmer Dashboard**: Interactive selection by:
  1. **Location / Agro-Climatic Zone** (Rayalaseema, Marathwada, Bundelkhand, North Karnataka, Western Rajasthan)
  2. **Crop & Growth Stage** (Groundnut, Cotton, Soybean, Bajra, Pigeonpea/Tur)
  3. **Advisory Type** (Emergency Drought Action, Irrigation & Water Conservation, Soil Health & Mulching, Organic Pest Defense)

---

## 🚀 Quickstart

### Prerequisites
1. [Ollama](https://ollama.com/) installed and running:
   ```bash
   ollama pull gemma2:2b
   ```
2. Python 3.9+ with Streamlit:
   ```bash
   pip install streamlit
   ```

### Launch the Dashboard
```bash
python -m streamlit run dharani_ai/app.py
```
