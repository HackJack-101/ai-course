import requests
from typing import Dict
from langchain_core.tools import tool


def get_system_message() -> str:
    return """You are a helpful weather assistant. 
        First, you need the current location, use the get_current_location tool.
        
        To answer questions about the current weather, you MUST use the get_current_weather tool with the location given by the get_current_location tool.
        DO NOT make up weather information on your own.
        DO NOT write code.
        """


@tool(
    name_or_callable="get_current_location",
    description="Get the current location of the user",
    return_direct=False,
)
def get_current_location() -> Dict:
    base_url = "https://freeipapi.com/api/json"

    try:
        response = requests.get(base_url)
        response.raise_for_status()

        data = response.json()

        location = f"{data['cityName']}, {data['countryName']}"

        print(f"get_current_location {location}")

        return {"location": location}

    except Exception as e:
        return {
            "error": f"Failed to current location: {str(e)}",
        }
