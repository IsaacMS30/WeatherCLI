import click

@click.group()
def cli():
    """WeatherCLI - A simple command line weather tool."""

@cli.command()
def hello():
    click.echo("Hola! WeatherCLI está funcionando.")
