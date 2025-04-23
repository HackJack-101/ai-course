import sys

from langchain_core.prompts import MessagesPlaceholder
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent

from courses.course_4.weather_tool import get_current_weather


def ask_weather_using_ollama(location: str):
    llm = ChatOllama(model="mistral", temperature=0.2)
    print(f"Location asked: {location}")

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a helpful weather assistant. 
        To answer questions about the current weather, you MUST use the get_current_weather tool.
        DO NOT make up weather information on your own.
        """,
            ),
            MessagesPlaceholder("messages"),
        ]
    )

    agent_executor = create_react_agent(
        llm, [get_current_weather], prompt=prompt, debug=False
    )
    query = f"I am in: {location}. Do I neet to wear a rain coat?"
    messages = agent_executor.invoke(
        {
            "messages": [
                ("human", query),
            ]
        }
    )
    # Take the last message
    output = messages["messages"][-1].content

    return output


def main():
    if len(sys.argv) < 2:
        print("Please provide location as argument")
        sys.exit(1)

    location = sys.argv[1]
    weather_response = ask_weather_using_ollama(location)
    print("\nFinal Response:")
    print(weather_response)
