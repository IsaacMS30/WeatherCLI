import requests

def fetch_json(url: str, params: dict) -> dict | None:
    try:
        response = requests.get(url, params=params, timeout=8)

        response.raise_for_status()

        data = response.json()

        return data

    except requests.exceptions.Timeout:
        print("Error: Timeout exceeded.")
        return None

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Conection error: {e}")
        return None

    except ValueError:
        print("Error: Response did not contain valid JSON.")
        return None
