"""
DharaniAI Intelligence Engine - Connects Gemma 2 to Micro-Climate Physics & Agronomy RAG.
100% Offline & Edge-Ready via Ollama.
"""

import json
import urllib.request
import urllib.error
from typing import Dict, Any, Generator

OLLAMA_API_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "gemma2:2b"

LANGUAGE_MAP = {
    "Telugu (తెలుగు)": {"code": "te", "instruction": "Provide your entire response in clear, warm, conversational Telugu (తెలుగు) suitable for Andhra Pradesh and Telangana farmers."},
    "Hindi (हिन्दी)": {"code": "hi", "instruction": "Provide your entire response in simple, conversational Hindi (हिन्दी) for farmers across Bundelkhand, UP, and MP."},
    "Marathi (मराठी)": {"code": "mr", "instruction": "Provide your entire response in clear, conversational Marathi (मराठी) for Marathwada and Vidarbha farmers."},
    "Kannada (ಕನ್ನಡ)": {"code": "kn", "instruction": "Provide your entire response in clear, conversational Kannada (ಕನ್ನಡ) for North Karnataka farmers."},
    "English": {"code": "en", "instruction": "Provide your response in clear, accessible English with simple agrarian terminology."}
}

SYSTEM_PROMPT = """You are DharaniAI (ధరణి / धरणी), an expert Senior Dryland Agronomist and Micro-Climate Specialist dedicated to supporting smallholder Indian farmers in drought-prone regions.

Your advice must be:
1. **Scientifically Rigorous & Actionable**: Direct, precise measurements (e.g. grams per liter, exact irrigation timing post-sunset, liters of water required).
2. **Empathetic & Clear**: Structured with clear headers, bullet points, and step-by-step instructions.
3. **Climate-Resilient & Practical**: Focus on low-cost, organic, and accessible Indian farming practices (ICAR/CRIDA guidelines, Jeevamrutha, mulching, anti-transpirants).
4. **Structured Format**:
   - 🚨 Current Threat Assessment (Explain what the VPD and temperature mean right now)
   - 🛡️ Immediate Action Plan (Next 24 to 48 Hours)
   - 💧 Water Conservation & Irrigation Guidance
   - 🌿 Organic Soil & Crop Shield
   - 💡 Farmer Wisdom Pro-Tip
"""

def build_dharani_prompt(
    region_name: str,
    crop_name: str,
    growth_stage: str,
    suggestion_type: str,
    climate_data: Dict[str, Any],
    agronomy_info: Dict[str, Any],
    custom_notes: str = "",
    target_lang: str = "Telugu (తెలుగు)"
) -> str:
    """Builds the comprehensive RAG prompt with climate physics and agronomy guidelines."""
    
    reg = agronomy_info["region"]
    crop = agronomy_info["crop"]
    lang_info = LANGUAGE_MAP.get(target_lang, LANGUAGE_MAP["Telugu (తెలుగు)"])
    
    prompt = f"""{SYSTEM_PROMPT}

LANGUAGE REQUIREMENT:
{lang_info['instruction']}

[FARM & REGIONAL PROFILE]
- Region: {region_name}
- Agro-Climatic Zone: {reg['climate']}
- Soil Profile: {reg['soil']}
- Historical Rainfall: {reg['annual_rainfall_mm']}
- Regional Priorities: {", ".join(reg['drought_mitigation_priorities'])}

[CROP & STAGE PROFILE]
- Crop: {crop_name} ({crop.get('scientific_name', '')})
- Current Growth Stage: {growth_stage}
- Critical Water Sensitivity Stages: {", ".join(crop['critical_water_stages'])}
- Inherent Drought Vulnerability: {crop['vulnerability_to_drought']}
- Official ICAR/CRIDA Emergency Recipe: {crop['emergency_recipe']}
- Organic & Regenerative Practices: {crop['organic_remedies']}

[LIVE MICRO-CLIMATE METRICS (PHYSICS ENGINE)]
- Ambient Temperature: {climate_data['temp_c']} °C
- Relative Humidity: {climate_data['humidity']}%
- Consecutive Dry Days (No Rain): {climate_data['dry_days']} days
- Calculated Vapor Pressure Deficit (VPD): {climate_data['vpd']} kPa
- Calculated Reference Evapotranspiration (ET0): {climate_data['et0']} mm/day (~{int(climate_data['et0'] * 10000)} Liters/hectare/day evaporative loss)
- Drought & Heat Stress Risk Category: {climate_data['risk_level']}
- Potential Yield Loss Vulnerability: {climate_data['loss_risk']}

[FOCUS ADVISORY AREA]
{suggestion_type}

[ADDITIONAL FARMER OBSERVATIONS]
{custom_notes if custom_notes.strip() else "None provided (standard field conditions)."}

Please deliver your detailed, step-by-step agricultural advisory now in {target_lang}:"""
    return prompt

def stream_dharani_advisory(
    region_name: str,
    crop_name: str,
    growth_stage: str,
    suggestion_type: str,
    climate_data: Dict[str, Any],
    agronomy_info: Dict[str, Any],
    custom_notes: str = "",
    target_lang: str = "Telugu (తెలుగు)",
    model: str = DEFAULT_MODEL
) -> Generator[str, None, None]:
    """Streams the advisory response token-by-token from local Gemma 2."""
    
    prompt = build_dharani_prompt(
        region_name, crop_name, growth_stage, suggestion_type,
        climate_data, agronomy_info, custom_notes, target_lang
    )
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True,
        "options": {
            "temperature": 0.35,
            "num_predict": 1200
        }
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_API_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            for line in response:
                if line:
                    chunk = json.loads(line.decode("utf-8"))
                    yield chunk.get("response", "")
                    if chunk.get("done", False):
                        break
    except urllib.error.URLError as e:
        yield f"\n[Network Error: Unable to communicate with local Ollama engine at {OLLAMA_API_URL}. Ensure Ollama is running. Error: {e}]"
