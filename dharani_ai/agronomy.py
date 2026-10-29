"""
Dryland Agronomy Knowledge Base for Indian Arid & Semi-Arid Belts.
Derived from ICAR & CRIDA (Central Research Institute for Dryland Agriculture) contingency guidelines.
"""

from typing import Dict, Any, List

REGIONS = {
    "Rayalaseema (Anantapur / Kurnool, AP)": {
        "climate": "Arid / Semi-Arid Deccan Rain Shadow",
        "soil": "Red sandy loam (low water retention) & Black Cotton",
        "primary_crops": ["Groundnut (TMV-2 / K-6)", "Pearl Millet (Bajra)", "Red Gram", "Castor"],
        "typical_weather": {"temp_c": 39.5, "humidity": 28.0, "dry_days": 18},
        "annual_rainfall_mm": "550mm (erratic)",
        "drought_mitigation_priorities": [
            "Protective life-saving irrigation at pod development stage",
            "Foliar spray of 1% Potassium Nitrate (KNO3) during 15+ day dry spells",
            "Broad-Bed and Furrow (BBF) moisture conservation",
            "Intercropping Groundnut with Red Gram (7:1 ratio)"
        ]
    },
    "Marathwada (Latur / Beed / Osmanabad, MH)": {
        "climate": "Severe Rain Shadow, High Evapotranspiration",
        "soil": "Medium to Deep Black Cotton Soil (high shrinkage/cracking)",
        "primary_crops": ["Soybean", "Cotton (Bt)", "Pigeonpea (Tur)", "Sorghum (Jowar)"],
        "typical_weather": {"temp_c": 41.0, "humidity": 22.0, "dry_days": 22},
        "annual_rainfall_mm": "650mm",
        "drought_mitigation_priorities": [
            "Foliar spray of 2% Urea or DAP to prevent nitrogen deficiency during prolonged dry spell",
            "Opening dead furrows after every 4 rows for in-situ rainwater harvesting",
            "Straw / biomass mulching to prevent deep soil cracking and moisture escape",
            "Drip irrigation pulse watering scheduled exclusively post-sunset (after 7 PM)"
        ]
    },
    "Bundelkhand (Jhansi / Mahoba / Banda, UP/MP)": {
        "climate": "Hyperthermic Arid with Rocky Outcrops",
        "soil": "Rakar (rocky eroded soil) & Kabar (black clay)",
        "primary_crops": ["Sesame (Til)", "Black Gram (Urad)", "Mustard", "Chickpea (Gram)"],
        "typical_weather": {"temp_c": 42.5, "humidity": 18.0, "dry_days": 25},
        "annual_rainfall_mm": "700mm (extreme variation)",
        "drought_mitigation_priorities": [
            "Farm pond (Khet Talab) water harvesting for critical single life-saving irrigation",
            "Deep summer tillage to improve percolation before monsoon",
            "Seed treatment with Trichoderma & Rhizobium to enhance deep root penetration",
            "Switching late-sown crops to short-duration drought-hardy pulses (e.g., T-9 Urad)"
        ]
    },
    "North Karnataka (Vijayapura / Bagalkot / Koppal, KA)": {
        "climate": "Dry Deccan Plateau",
        "soil": "Deep Black Vertisols & Gravelly Red Soil",
        "primary_crops": ["Rabi Sorghum (Maldandi)", "Sunflower", "Bengal Gram", "Green Gram"],
        "typical_weather": {"temp_c": 38.0, "humidity": 30.0, "dry_days": 16},
        "annual_rainfall_mm": "580mm",
        "drought_mitigation_priorities": [
            "Compartmental bunding before monsoon showers",
            "Kaolin clay spray (5%) as an anti-transpirant to reflect harsh solar radiation",
            "Dust mulching by inter-culturing with hoes to break capillary action",
            "Staggered planting with drought-tolerant varieties"
        ]
    },
    "Western Rajasthan (Jodhpur / Barmer / Bikaner, RJ)": {
        "climate": "Hyper-Arid Thar Desert Border",
        "soil": "Desert Sandy Soil (very rapid infiltration, almost zero organic matter)",
        "primary_crops": ["Pearl Millet (Bajra)", "Moth Bean", "Cluster Bean (Guar)", "Cumin"],
        "typical_weather": {"temp_c": 44.0, "humidity": 14.0, "dry_days": 30},
        "annual_rainfall_mm": "310mm",
        "drought_mitigation_priorities": [
            "Shelterbelts and micro-windbreaks with Khejri (Prosopis cineraria) trees",
            "Hydrogel application at sowing to absorb and slowly release moisture",
            "Strict sub-surface drip irrigation to prevent surface heat vaporization",
            "Inter-row rainwater conservation with plastic or gravel mulches"
        ]
    }
}

CROPS_DATABASE = {
    "Groundnut": {
        "scientific_name": "Arachis hypogaea",
        "stages": ["Sowing & Germination (0-15 DAS)", "Vegetative (15-30 DAS)", "Flowering & Pegging (30-50 DAS)", "Pod Development (50-75 DAS)", "Maturity (75-105 DAS)"],
        "critical_water_stages": ["Flowering & Pegging", "Pod Development"],
        "vulnerability_to_drought": "Extremely high during peg penetration and pod formation; moisture deficit results in 'pops' (hollow pods with no kernel).",
        "water_requirement_mm": "450 - 650 mm",
        "organic_remedies": "Jeevamrutha foliar spray (5% dilution) every 10 days to encourage soil mycorrhizae; neem oil (3000 ppm) @ 3ml/L against red hairy caterpillar during heat spells.",
        "emergency_recipe": "Foliar spray with 1% Potassium Nitrate (KNO3, 10g/L) + 0.5% Zinc Sulphate to restore leaf turgidity during mid-season dry spells."
    },
    "Soybean": {
        "scientific_name": "Glycine max",
        "stages": ["Germination", "Vegetative V1-V4", "Flowering R1-R2", "Pod Formation R3-R4", "Seed Filling R5-R6"],
        "critical_water_stages": ["Flowering R1-R2", "Pod-filling R5"],
        "vulnerability_to_drought": "High sensitivity during flowering. Ambient temperatures above 38°C cause massive flower abortion and poor pod set.",
        "water_requirement_mm": "450 - 700 mm",
        "organic_remedies": "Panchagavya (3% spray) at branching and flowering; straw mulching @ 5 tons/ha to lower soil surface temperatures by up to 4°C.",
        "emergency_recipe": "Foliar spray of 13-0-45 (Multi-K) @ 5g per liter water. Suspend all non-selective chemical weedicides during moisture stress."
    },
    "Cotton (Bt)": {
        "scientific_name": "Gossypium hirsutum",
        "stages": ["Seedling", "Square Formation", "Flowering", "Boll Development", "Boll Bursting"],
        "critical_water_stages": ["Square Formation", "Flowering & Boll Development"],
        "vulnerability_to_drought": "Moderate in early stages due to deep taproot; high during boll loading. Water stress triggers boll drop and square drying.",
        "water_requirement_mm": "700 - 1200 mm",
        "organic_remedies": "Vermicompost top dressing @ 250 kg/acre combined with biochar to increase soil water retention capacity.",
        "emergency_recipe": "Alternate furrow irrigation (saves 50% water while maintaining root zone moisture). Foliar spray of 2% DAP + 1% MgSO4 + Planofix (NAA) @ 4ml/15L."
    },
    "Pearl Millet (Bajra)": {
        "scientific_name": "Pennisetum glaucum",
        "stages": ["Seedling", "Tillering", "Stem Elongation", "Booting / Heading", "Grain Maturity"],
        "critical_water_stages": ["Tillering", "Booting / Grain-filling"],
        "vulnerability_to_drought": "Low; resilient C4 photosynthetic mechanism with extraordinary water-use efficiency.",
        "water_requirement_mm": "250 - 350 mm",
        "organic_remedies": "Farmyard Manure (FYM) incorporation @ 10 tons/ha prior to sowing; intercropping with Cowpea or Moth Bean to maintain living ground cover.",
        "emergency_recipe": "Crop thinning: physically remove 20-25% of weaker plants in each row to reduce canopy transpirational surface area and conserve residual moisture."
    },
    "Pigeonpea (Tur / Red Gram)": {
        "scientific_name": "Cajanus cajan",
        "stages": ["Early Vegetative", "Branching", "Flower Bud Initiation", "Pod Formation", "Maturity"],
        "critical_water_stages": ["Branching", "Flowering & Pod Setting"],
        "vulnerability_to_drought": "Low during vegetative growth due to taproot reaching 2 meters depth; highly vulnerable to dry spells coinciding with pod filling.",
        "water_requirement_mm": "350 - 450 mm",
        "organic_remedies": "Rhizobium & PSB seed treatment; mulching with crushed dry pigeonpea stalks between rows.",
        "emergency_recipe": "Foliar spray of Kaolin clay (5% suspension) as a reflective antitranspirant to bounce sunlight and cool the canopy by 2-3°C."
    }
}

SUGGESTION_TYPES = {
    "Emergency Drought & Heat Action Plan": "Immediate 24-48 hour life-saving interventions (anti-transpirant sprays, emergency watering timing, flower drop prevention).",
    "Irrigation & Water Conservation Strategy": "Exact water volume estimation (liters/hectare), drip schedule, alternate furrow methods, and soil moisture locking.",
    "Soil Health, Mulching & Regenerative Care": "Compost, biochar, crop residue mulching, zero-till practices to build long-term soil organic carbon and sponge capacity.",
    "Organic Pest & Disease Defense under Heat Stress": "Natural biopesticide concoctions (Neem, Jeevamrutha, Dashaparni Kashayam) that will not scorch leaves under high UV/temperatures."
}
