import logging
from typing import Iterable

from openai import OpenAI
import instructor

from courses.config.logger import get_logger
from courses.course_2.data import get_sample_text
from courses.course_2.response import get_system_message, StandardizedCharacter

logger = get_logger(__name__, "DEBUG")

# Set logging to DEBUG
logging.basicConfig(level=logging.DEBUG)


def standardize_character_by_ai(text: str) -> Iterable[StandardizedCharacter]:
    client = instructor.from_openai(
        OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama",  # required, but unused
        ),
        mode=instructor.Mode.JSON,
    )

    response = client.chat.completions.create(
        model="mistral",
        messages=[
            get_system_message(),
            {
                "role": "user",
                "content": f"Here the expression to analyze : ```{text}```",
            },
        ],
        response_model=Iterable[StandardizedCharacter],
        temperature=0,
        max_retries=0,
    )

    return response


def main():
    return standardize_character_by_ai(get_sample_text())
