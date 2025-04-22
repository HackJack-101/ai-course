import sys
import subprocess

from openai import OpenAI
from pydantic import BaseModel
import instructor


class AnswerWithNecessaryCalculationAndFinalChoice(BaseModel):
    chain_of_thought: str
    necessary_calculations: list[str]
    potential_final_answers: list[str]
    answer: float


def chain_of_thought(
    question: str, model: str
) -> AnswerWithNecessaryCalculationAndFinalChoice:
    client = instructor.from_openai(
        OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama",  # required, but unused
        ),
        mode=instructor.Mode.JSON,
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": question,
            },
        ],
        response_model=AnswerWithNecessaryCalculationAndFinalChoice,
        temperature=0,
        max_retries=1,
    )

    return response


def help_message():
    print("Please provide model name as argument")
    print("\nAvailable models:")
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    print(result.stdout)
    sys.exit(1)


def dice():
    if len(sys.argv) < 2:
        return help_message()

    model_name = sys.argv[1]
    question = "You roll two dice. What’s the probability they add up to 7?"
    return chain_of_thought(question, model_name)


def physics():
    if len(sys.argv) < 2:
        return help_message()

    model_name = sys.argv[1]
    question = """The moon and the Earth are not at the same distance at any time. This distance varies between 356 000km and 406 000km.
     During the experiment, the Moon and the Earth are distant by 380 000km. Calculate the gravitational force between the Earth and the Moon in Newtons during the experiment.
     
     **Constants**
     - Mass of the Earth: 5.972 × 10^24 kg
     - Mass of the Moon: 7.348 × 10^22 kg
     - G : 6.6740 × 10^-11 N(m/kg)^2
     """
    return chain_of_thought(question, model_name)
