import click
from weathercli.services.geocoding import get_coordinates

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
    #information = get_weather_data(latitude, longitude)
    # Format output

