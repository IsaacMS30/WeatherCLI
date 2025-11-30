from rich.console import Console
from rich.table import Table, box
from weathercli.utils.weather_code import interpret_weather_code
from rich.theme import Theme

custom_theme = Theme({
    "title": "bold bright_cyan",
    "metric": "bold cyan",
    "value": "white",
    "warning": "bold red",
})

console = Console(theme=custom_theme)

def color_temp(temp: float):
    if temp < 10:
        return "bright_cyan"
    elif temp < 25:
        return "bright_green"
    else:
        return "bright_yellow"


def format_current_weather(weather_data: dict, city: str, country: str) -> None:
    table = Table(title=f"[title]Weather in {city}, {country}[/title]", box=box.ROUNDED)

    description, emoji = interpret_weather_code(weather_data["weathercode"])
    temp_color = color_temp(weather_data["temperature"])

    table.add_column("Metric", justify="center", style="metric")
    table.add_column("Value", justify="center", style="value")

    table.add_row("Condition", f"{description} {emoji}")
    table.add_row("Temperature", f"[{temp_color}]{weather_data['temperature']} °C[/]")
    table.add_row("Wind speed", f"{weather_data["windspeed"]} km/h")
    table.add_row("Wind direction", f"{weather_data["winddirection"]}°")
    table.add_row("Time", weather_data["time"])

    console.print(table)
