from pydantic import BaseModel, Field


class StandardizedCharacter(BaseModel):
    first_name: str
    last_name: str
    age: int
    country_code: str = Field(
        description="The ISO 3166-1 alpha-3 country code (e.g., USA, FRA, JPN)",
        pattern=r"[A-Z]{3}",
    )
    phone_number: str = Field(
        description="The phone number should be in the international format like +91 1234567890",
        pattern=r"\+[0-9]{0,3}[0-9]+",
    )


def get_system_message():
    return {
        "role": "system",
        "content": """
    You are a expression analysis expert tasked with extracting and standardizing character information from fictional expression.

    ## Task:
    Extract all unique characters from the provided expression and standardize their information according to the following specifications:

    ## Information to Extract:

    1. **Name:**
       - Extract both first and last names
       - Remove any titles (Mr., Mrs., Dr., Prof., etc.)
       - If only one name is provided, classify it as the first name

    2. **Age:**
       - Extract the numerical age of each character
       - If age is written as expression, convert it to a number

    3. **Location:**
       - Identify the city/location where the character resides
       - Determine the country based on the city
       - Provide the ISO 3166-1 alpha-3 country code according to this mapping:
         * United States → USA
         * France → FRA
         * Japan → JPN
         * United Kingdom → GBR
         * Germany → DEU
         * Italy → ITA
         * Spain → ESP
         * China → CHN
         * India → IND
         * Canada → CAN
         * Australia → AUS
         * Brazil → BRA
         * Russia → RUS
         * Mexico → MEX
         * For other countries, use the appropriate ISO 3166-1 alpha-3 code

    4. **Phone Number:**
       - Format all phone numbers with international format, remove all separators like `-`
       - Add the appropriate country code based on the character's location
       - Except the + character, all other characters should be numeric characters.
       - Example format: "+1 5559876" for a US number
    """,
    }
