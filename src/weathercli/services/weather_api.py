from weathercli.utils.http import fetch_json

def get_weather_data(lat: float, lon: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
    }

    data = fetch_json(url, params)

    if not data or "current_weather" not in data:
        return {"error": "Could not get weather information"}
    
    return data["current_weather"]

def get_weather_forecast(lat: float, lon: float, days: int = 3) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "weathercode,temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
    }

    data = fetch_json(url, params)

    if not data or "daily" not in data:
        return {"error": "Could not get weather information"}

    for key in data["daily"]:
        data["daily"][key] = data["daily"][key][:days]

    return data["daily"]
