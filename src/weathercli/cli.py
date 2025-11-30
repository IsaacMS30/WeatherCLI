import click
from weathercli.services.geocoding import get_coordinates
from weathercli.services.weather import get_weather_data

# TODO(me): Do help commands

@click.group()
def cli():
    """WeatherCLI - A simple command line weather tool."""

@cli.command()
@click.argument('city', nargs = 1)
@click.argument('country', nargs = 1)
def current(city: str, country: str):
    click.echo(f"Obtaining weather information...")
    # Get coordanates from the place
    coordinates = get_coordinates(city, country)

    if "error" in coordinates or coordinates is None:
        click.echo(f"Could not found coordinates for {city}, {country}")
    
    click.echo(f"Latitude: {coordinates["latitude"]}, longitude: {coordinates["longitude"]}")
    # Request information from API
    weather_info = get_weather_data(coordinates["latitude"], coordinates["longitude"])
    click.echo(weather_info)
    # Format output

