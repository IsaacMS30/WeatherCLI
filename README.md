# 🌤️ WeatherCLI — Command Line Weather Tool

WeatherCLI is a simple and elegant command-line application that provides weather information directly from your terminal.
It uses the Open-Meteo API, requires no API key, and is designed to be beginner-friendly and easy to extend.


## ✨ Features
- 🌡️ Get **current weather** for any city and country.
- 📅 Retrieve **7-day forecasts** with temperatures and precipitation.
- 🌎 Automatic geocoding (city + country → coordinates)
- 🎨 Pretty terminal formatting using **Rich**.
- 📦 Installable as a global command: weathercli

## 📦 Installation

Requires Python 3.10 or later.

Install the dependencies:
```bash
pip install -r requirements.txt
```

Install the tool locally in editable mode
```bash
pip install -e .
```

With this, tou can use the **weathercli** command in your terminal

## 🚀 Usage

### 🔹 Current Weather
```bash
weathercli current "New York" USA
```

### 🔹 Weather Forecast (1-7 days)
```bash
weathercli forecast Madrid Spain --days 5
```

## 🧠 CLI Help
```bash
weathercli --help
weathercli current --help
weathercli forecast --help
```

## 🙌 Acknowledgements

Open-Meteo — Free weather APIs: https://open-meteo.com

Click — Elegant command-line tools

Rich — Beautiful terminal formatting