import click
from weathercli.services.geocoding import get_coordinates
from weathercli.services.weather import get_weather_data
from weathercli.presentation.formatter import format_current_weather

# TODO(me): Do help commands

@click.group()
def cli():
    """WeatherCLI - A simple command line weather tool."""

@cli.command()
@click.argument('city', nargs = 1)
@click.argument('country', nargs = 1)
def current(city: str, country: str):
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
