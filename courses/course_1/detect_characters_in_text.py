from typing import Iterable

from openai import OpenAI
import instructor

from courses.course_1.response import get_system_message, Character


def detect_character_by_ai(text: str) -> Iterable[Character]:
    client = instructor.from_openai(
        OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama",  # required, but unused
        ),
        mode=instructor.Mode.JSON,
    )

    response = client.chat.completions.create(
        model="mistral:latest",
        messages=[
            get_system_message(),
            {
                "role": "user",
                "content": f'Novel expression : "{text}"',
            },
        ],
        response_model=Iterable[Character],
        temperature=0,
    )

    print(response)

    return response
