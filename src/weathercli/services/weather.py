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
