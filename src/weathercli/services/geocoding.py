import requests
from weathercli.utils.country_code import get_country_code

def get_coordinates(city: str, country:str) -> dict:
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
    response = requests.get(url=url, params=params)
    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        return {"error": f"No coordenates found for f{city}, {country}"}
    
    result = data["results"][0]

    # Return coordinates
    # !! Can return elevation, population or other information in the future
    return {
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }
