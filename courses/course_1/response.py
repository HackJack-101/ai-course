from pydantic import BaseModel


def get_system_message():
    return {
        "role": "system",
        "content": "You are a novel analyst. You have to find all unique characters in a fictional expression and extract their name, age and phone number.",
    }


class Character(BaseModel):
    first_name: str
    last_name: str
    age: int
    phone_number: str
