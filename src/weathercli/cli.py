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
    click.echo(f"Country: {country}, city: {city}")
    # Get coordanates from the place
    coordinates = get_coordinates(city, country)

    if "error" in coordinates or coordinates is None:
        click.echo(f"Could not found coordinates for {city}, {country}")
    
    
    # Request information from API
    # Format output

