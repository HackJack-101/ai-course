import logging
import re

from openai import OpenAI
from pydantic import BaseModel
import instructor

from courses.config.logger import get_logger

logger = get_logger(__name__, "DEBUG")

# Set logging to DEBUG
logging.basicConfig(level=logging.DEBUG)


class AlgebraResponse(BaseModel):
    chain_of_thought: str
    necessary_calculations: list[str]
    answer: str


def solve_algebra(expression: str) -> AlgebraResponse:
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
            {
                "role": "system",
                "content": """
You are a math calculator. User will give you an algebraic expression and you have to solve it.
You have to respect PEMDAS.

The answer should be written as a python function like this:

```python
def answer():
    return 3**2+(7+*5)-4
``` 

""",
            },
            {
                "role": "user",
                "content": f"Here the algebraic expression to answer: ```{expression}```",
            },
        ],
        response_model=AlgebraResponse,
        temperature=0,
        max_retries=0,
    )

    return response


def extract_after_return(text: str) -> str | None:
    match = re.search(r"return\s*(.*)", text)
    if match:
        return match.group(1).strip()
    else:
        return None


def apply_calculations(python_function: str) -> int:
    response = extract_after_return(python_function)
    if response is None:
        return 0

    return eval(response)


def main():
    return solve_algebra("(3 + 2) ^ 2 - 4 * 2")
