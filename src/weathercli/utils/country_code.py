import pycountry

def get_country_code(country_name: str) -> str | None:
    try:
        # Fuzzy coincidences
        results = pycountry.countries.search_fuzzy(country_name)

        if not results:
            return None

        best_match = results[0]
        return best_match.alpha_2

    except LookupError:
        return None
