import click
from weathercli.services.geocoding import get_coordinates
from weathercli.services.weather_api import get_weather_data, get_weather_forecast
from weathercli.presentation.formatter import format_current_weather, format_weather_forecast

# TODO(me): Do help commands

@click.group()
def cli():
    """WeatherCLI - A simple command line weather tool."""


@cli.command()
@click.argument('city', nargs = 1)
@click.argument('country', nargs = 1)
def current(city: str, country: str) -> None:
    click.echo(f"Obtaining weather information...\n\n")

    # Get coordanates from the place
    coordinates = get_coordinates(city, country)

    if "error" in coordinates or coordinates is None:
        click.echo(f"Could not found coordinates for {city}, {country}")
        return

    # Request information from API
    weather_data = get_weather_data(coordinates["latitude"], coordinates["longitude"])

    if "error" in weather_data:
        click.echo(f"Could not get weather information for {city}, {country}")
        return

    # Format output
    format_current_weather(weather_data, city, country)


@cli.command()
@click.argument('city', nargs = 1)
@click.argument('country', nargs = 1)
@click.option("--days", default=3, help="Number of days to show (max 7)")
def forecast(city: str, country:str, days:int) -> None:
    # Verify days parameter
    if days < 1 or days > 7:
        raise click.BadParameter("Days must be between 1 and 7")

    # Get coordanates from the place
    coordinates = get_coordinates(city, country)

    if "error" in coordinates or coordinates is None:
        click.echo(f"Could not found coordinates for {city}, {country}")
        return

    # Request information from API
    forecast_data = get_weather_forecast(coordinates["latitude"], coordinates["longitude"], days)

    if "error" in forecast_data:
        click.echo(f"Could not get weather information for {city}, {country} (next {days} days)")
        return

    # Format output
    format_weather_forecast(forecast_data, city, country, days)
