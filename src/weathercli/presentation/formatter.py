from rich.console import Console
from rich.table import Table, box
from weathercli.utils.weather_code import interpret_weather_code
from rich.theme import Theme
from datetime import datetime

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

def from_date_to_day(date: str) -> str:
    date_object = datetime.strptime(date, "%Y-%m-%d")

    return(date_object.strftime("%A"))


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
    table.add_row("Time", "☀️" if weather_data["is_day"] else "🌙")

    console.print(table)

def format_weather_forecast(forecast_data: dict, city: str, country: str, days: int) -> None:
    table = Table(title=f"[title]Weather in {city}, {country} (next {days} days)[/title]", box=box.ROUNDED)

    table.add_column("Day", justify="center", style="metric")
    table.add_column("Min Temp", justify="center", style="value")
    table.add_column("Max Temp", justify="center", style="value")
    table.add_column("Condition", justify="center", style="value")

    for i in range(days):
        day = from_date_to_day(forecast_data["time"][i])
        weather_code = forecast_data["weathercode"][i]
        min_temp = forecast_data["temperature_2m_min"][i]
        max_temp = forecast_data["temperature_2m_max"][i]

        description, emoji = interpret_weather_code(weather_code)
        max_temp_color = color_temp(max_temp)
        min_temp_color = color_temp(min_temp)
        table.add_row(day, f"[{min_temp_color}]{min_temp} °C[/]", f"[{max_temp_color}]{max_temp} °C[/]", f"{description} {emoji}")

    console.print(table)

