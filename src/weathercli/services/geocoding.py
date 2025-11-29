from weathercli.utils.http import fetch_json
from weathercli.utils.country_code import get_country_code

def get_coordinates(city: str, country:str) -> dict | None:
    # Get country code
    country_code = get_country_code(country)

    # Request coordinates
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count": 10,
        "countryCode": country_code
    }

    # Process coordinates
    data = fetch_json(url, params)

    if not data or "results" not in data:
        return {"error": f"No coordenates found for f{city}, {country}"}
    
    result = data["results"][0]

    # Return coordinates
    # !! Can return elevation, population or other information in the future
    return {
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }
