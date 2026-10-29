"""
Micro-Climate Physics & Evapotranspiration Calculations for Indian Drylands.
Implements FAO-56 and Agro-meteorological equations for drought vulnerability.
"""

import math
from typing import Dict, Any

def calculate_saturation_vapor_pressure(temp_c: float) -> float:
    """Calculates saturation vapor pressure (es) in kPa using Tetens equation."""
    return 0.61078 * math.exp((17.27 * temp_c) / (temp_c + 237.3))

def calculate_actual_vapor_pressure(temp_c: float, humidity_percent: float) -> float:
    """Calculates actual vapor pressure (ea) in kPa."""
    es = calculate_saturation_vapor_pressure(temp_c)
    return es * (humidity_percent / 100.0)

def calculate_vpd(temp_c: float, humidity_percent: float) -> float:
    """
    Calculates Vapor Pressure Deficit (VPD) in kPa.
    VPD = es - ea
    """
    es = calculate_saturation_vapor_pressure(temp_c)
    ea = calculate_actual_vapor_pressure(temp_c, humidity_percent)
    return max(0.0, es - ea)

def calculate_et0_hargreaves(t_mean: float, t_max: float, t_min: float, latitude: float = 17.5) -> float:
    """
    Estimates daily Reference Evapotranspiration (ET0) in mm/day
    using the FAO Hargreaves-Samani method for data-scarce dryland regions.
    Latitude defaults to ~17.5°N (covers Deccan Plateau / Marathwada / Rayalaseema).
    """
    # Extraterrestrial solar radiation (Ra) approximation for tropical Indian latitudes (~15 mm/day eq)
    ra_equivalent = 15.2
    temp_range = max(0.1, t_max - t_min)
    
    # Hargreaves formula: ET0 = 0.0023 * (Tmean + 17.8) * (Tmax - Tmin)^0.5 * Ra
    et0 = 0.0023 * (t_mean + 17.8) * math.sqrt(temp_range) * ra_equivalent
    return round(max(0.5, et0), 2)

def assess_climate_stress(temp_c: float, humidity_percent: float, dry_days: int) -> Dict[str, Any]:
    """
    Computes climate stress scores and classifies drought risk levels.
    """
    vpd = round(calculate_vpd(temp_c, humidity_percent), 2)
    
    # Drought & Heat Stress Classification
    if vpd > 2.5 or dry_days >= 21 or temp_c >= 42:
        risk_level = "CRITICAL / SEVERE DROUGHT"
        risk_color = "#e53e3e"
        status_code = "RED"
        loss_risk = "Severe (40% - 70% yield loss if unmitigated)"
    elif vpd > 1.8 or dry_days >= 14 or temp_c >= 38:
        risk_level = "HIGH HEAT & MOISTURE STRESS"
        risk_color = "#dd6b20"
        status_code = "ORANGE"
        loss_risk = "Moderate (20% - 40% yield drop)"
    elif vpd > 1.2 or dry_days >= 7:
        risk_level = "MODERATE WATCH"
        risk_color = "#d69e2e"
        status_code = "YELLOW"
        loss_risk = "Mild (5% - 15% stress)"
    else:
        risk_level = "OPTIMAL / LOW STRESS"
        risk_color = "#38a169"
        status_code = "GREEN"
        loss_risk = "Minimal (< 5%)"

    return {
        "vpd_kpa": vpd,
        "risk_level": risk_level,
        "status_code": status_code,
        "risk_color": risk_color,
        "loss_risk": loss_risk
    }