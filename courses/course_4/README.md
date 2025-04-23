# Weather

We are using tools with LLM to get current weather data in a given location. 

## Requirements

- Create a free account at https://openweathermap.org/ to get an API key
- Fill `courses/config/open_weather.py` with this key

## Exercice

- Open `weather_here.py`
- This agent must get your current location to find the current weather
- Create `get_current_location` tool with https://freeipapi.com/api/json to get the city and the country of your estimated location
- `poetry run course-4-here` have to return the current weather

### Tips

- The system message can be modified if you need
- The temperature can be modified if you need