import requests
from typing import Dict
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from courses.config.open_weather import get_api_key


class WeatherInput(BaseModel):
    location: str = Field(description="The city and state, e.g. San Francisco, CA")


@tool(
    name_or_callable="get_current_weather",
    description="Get the current weather in a given location",
    args_schema=WeatherInput,
    return_direct=False,
)
def get_current_weather(location: str) -> Dict:
    api_key = get_api_key()
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    print(f"Fetching weather data for: {location}")

    try:
        params = {
            "q": location,
            "appid": api_key,
            "units": "metric",
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        print(data)

        weather_data = {
            "location": location,
            "temperature": f"{data['main']['temp']}°C",
            "condition": data["weather"][0]["description"].capitalize(),
            "humidity": f"{data['main']['humidity']}%",
            "wind": f"{data['wind']['speed']} m/s",
            "feels_like": f"{data['main']['feels_like']}°C",
            "sunrise_utc_timestamp": f"{data['sys']['sunrise']}",
            "sunset_utc_timestamp": f"{data['sys']['sunset']}",
        }

        return weather_data

    except requests.exceptions.RequestException as e:
        return {
            "error": f"Failed to fetch weather data: {str(e)}",
            "location": location,
        }
    except (KeyError, ValueError, TypeError) as e:
        return {
            "error": f"Failed to parse weather data: {str(e)}",
            "location": location,
        }
