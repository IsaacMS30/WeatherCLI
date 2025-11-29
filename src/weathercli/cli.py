import click

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
    # Request information from API
    # Format output

