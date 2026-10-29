"""
DharaniAI (ధరణి / धरणी): Offline Climate Resilience & Drought Advisory System
Full Interactive Streamlit Dashboard with Native Voice / Audio for Indian Smallholder Farmers.
"""

import streamlit as st
from dharani_ai.physics import assess_climate_stress, calculate_et0_hargreaves
from dharani_ai.agronomy import REGIONS, CROPS_DATABASE, SUGGESTION_TYPES
from dharani_ai.engine import stream_dharani_advisory, DEFAULT_MODEL, LANGUAGE_MAP
from dharani_ai.audio import generate_native_speech

st.set_page_config(
    page_title="DharaniAI | Offline Drought & Climate Resilience for Farmers",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling: Earthy, warm agrarian palette (sun gold, deep foliage green, terra cotta)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #0d1611 0%, #15221b 100%);
        color: #edf2f7;
    }
    h1, h2, h3 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #f6ad55 !important;
    }
    .metric-card {
        background-color: rgba(30, 48, 38, 0.7);
        border: 1px solid #3c634c;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 12px;
    }
    .danger-alert {
        background-color: rgba(155, 44, 44, 0.35);
        border-left: 5px solid #fc8181;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 15px;
    }
    .success-alert {
        background-color: rgba(39, 103, 73, 0.35);
        border-left: 5px solid #68d391;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.title("🌾 DharaniAI (ధరణి / धरणी)")
st.markdown("### *Offline Climate Resilience, Micro-Weather Physics & Native Voice Advisory for Farmers* 🔊")
st.markdown("##### 📍 Focused on vulnerable belts: *Rayalaseema, Marathwada, Bundelkhand, North Karnataka & Thar Border*")
st.markdown("---")

# Sidebar: Farmer & Farm Configuration
with st.sidebar:
    st.header("🚜 Farm Configuration")
    
    # 0. Choose Language
    st.subheader("🗣️ Native Language (భాష / भाषा)")
    selected_language = st.selectbox(
        "Select Farmer Voice Language:",
        list(LANGUAGE_MAP.keys()),
        index=0  # Default to Telugu
    )
    st.markdown("---")
    
    # 1. Choose Location
    st.subheader("1. Location & Agro-Climatic Zone")
    selected_region = st.selectbox(
        "Select Drought-Prone Region:",
        list(REGIONS.keys())
    )
    reg_data = REGIONS[selected_region]
    
    st.caption(f"**Soil:** {reg_data['soil']}")
    st.caption(f"**Rainfall:** {reg_data['annual_rainfall_mm']}")
    st.markdown("---")
    
    # 2. Choose Crop
    st.subheader("2. Crop & Growth Stage")
    selected_crop = st.selectbox(
        "Select Cultivated Crop:",
        list(CROPS_DATABASE.keys())
    )
    crop_data = CROPS_DATABASE[selected_crop]
    
    selected_stage = st.selectbox(
        "Current Growth Stage:",
        crop_data["stages"]
    )
    st.markdown("---")
    
    # 3. Choose Suggestion Type
    st.subheader("3. Advisory Focus")
    selected_suggestion_type = st.selectbox(
        "Choose Guidance Type:",
        list(SUGGESTION_TYPES.keys())
    )
    st.caption(SUGGESTION_TYPES[selected_suggestion_type])
    st.markdown("---")
    
    st.info(f"🔮 **Inference:** Local `Google {DEFAULT_MODEL}`\n\n📶 **Offline Mode:** 100% active (Zero Internet Required)")

# Main Panel: Two Columns
col_metrics, col_advisory = st.columns([1.0, 1.4], gap="large")

with col_metrics:
    st.subheader("☀️ Real-Time Micro-Climate & Physics")
    st.markdown("Adjust to match your current local field weather conditions:")
    
    col_t, col_h = st.columns(2)
    with col_t:
        temp_input = st.slider("Field Temp (°C)", min_value=20.0, max_value=50.0, value=float(reg_data["typical_weather"]["temp_c"]), step=0.5)
    with col_h:
        hum_input = st.slider("Relative Humidity (%)", min_value=10.0, max_value=100.0, value=float(reg_data["typical_weather"]["humidity"]), step=1.0)
        
    dry_days_input = st.slider("Consecutive Dry Days (Days without rain)", min_value=0, max_value=60, value=int(reg_data["typical_weather"]["dry_days"]), step=1)
    
    # Physics Calculations
    stress_assessment = assess_climate_stress(temp_input, hum_input, dry_days_input)
    et0_val = calculate_et0_hargreaves(t_mean=temp_input - 3.0, t_max=temp_input, t_min=max(18.0, temp_input - 10.0))
    water_loss_liters_ha = int(et0_val * 10000)
    
    # Metric Display Cards
    m1, m2 = st.columns(2)
    with m1:
        st.metric(label="Vapor Pressure Deficit (VPD)", value=f"{stress_assessment['vpd_kpa']} kPa", delta="Atmospheric Thirst", delta_color="inverse")
    with m2:
        st.metric(label="Daily Evaporative Water Loss", value=f"{et0_val} mm/day", delta=f"{water_loss_liters_ha:,} L/ha/day", delta_color="inverse")
        
    # Stress Classification Alert
    if stress_assessment["status_code"] in ["RED", "ORANGE"]:
        st.markdown(f"""
        <div class="danger-alert">
            <h4 style="color: #fc8181; margin: 0 0 5px 0;">⚠️ {stress_assessment['risk_level']}</h4>
            <p style="margin: 0; font-size: 0.95em;"><b>Estimated Yield Loss Risk:</b> {stress_assessment['loss_risk']}<br>
            <i>Extreme atmospheric demand forces plant stomata to shut down, halting photosynthesis and causing flower drop.</i></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="success-alert">
            <h4 style="color: #68d391; margin: 0 0 5px 0;">✅ {stress_assessment['risk_level']}</h4>
            <p style="margin: 0; font-size: 0.95em;"><b>Estimated Yield Loss Risk:</b> {stress_assessment['loss_risk']}</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📖 Regional ICAR / CRIDA Contingencies & Priorities", expanded=True):
        st.write(f"**Key Focus for {selected_region}:**")
        for prio in reg_data["drought_mitigation_priorities"]:
            st.write(f"• {prio}")
            
    custom_notes = st.text_area(
        "Optional Farmer Field Observations (e.g. leaf yellowing, borewell water drop):",
        placeholder="e.g. My cotton leaves are wilting in afternoon sun and lower leaves turning yellow...",
        height=80
    )
    
    generate_btn = st.button("🌱 Generate Precision Climate Advisory & Voice", type="primary", use_container_width=True)

with col_advisory:
    st.subheader(f"📋 Precision Agronomic Advisory ({selected_language})")
    
    if generate_btn:
        climate_summary = {
            "temp_c": temp_input,
            "humidity": hum_input,
            "dry_days": dry_days_input,
            "vpd": stress_assessment["vpd_kpa"],
            "et0": et0_val,
            "risk_level": stress_assessment["risk_level"],
            "loss_risk": stress_assessment["loss_risk"]
        }
        
        agronomy_summary = {
            "region": reg_data,
            "crop": crop_data
        }
        
        with st.status(f"🧠 Synthesizing Micro-Climate Physics, ICAR Guidelines & Local Gemma 2 in {selected_language}...", expanded=True) as status:
            response_container = st.empty()
            full_text = ""
            
            for chunk in stream_dharani_advisory(
                region_name=selected_region,
                crop_name=selected_crop,
                growth_stage=selected_stage,
                suggestion_type=selected_suggestion_type,
                climate_data=climate_summary,
                agronomy_info=agronomy_summary,
                custom_notes=custom_notes,
                target_lang=selected_language
            ):
                full_text += chunk
                response_container.markdown(full_text + " ▌")
                
            response_container.markdown(full_text)
            status.update(label="✅ Advisory Generated Successfully!", state="complete")

        # Native Voice Audio Generation
        st.markdown("---")
        st.subheader("🔊 Listen to Audio Advisory (రైతు కోసం వాయిస్ / किसान के लिए आवाज)")
        with st.spinner("🎙️ Synthesizing native voice audio..."):
            lang_code = LANGUAGE_MAP[selected_language]["code"]
            audio_path = generate_native_speech(full_text, lang=lang_code)
            if audio_path:
                st.audio(audio_path, format="audio/mp3")
                st.caption(f"🎧 Playing audio synthesized in **{selected_language}**.")
            else:
                st.info("Audio playback is available when offline TTS or speaker output is configured.")
    else:
        st.info("👈 Select your location, crop, language, and advisory focus on the left, then click **'Generate Precision Climate Advisory & Voice'** to receive customized guidance.")
