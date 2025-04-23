from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent

from courses.course_4.response import get_current_location
from courses.course_4.weather_tool import get_current_weather


def ask_current_weather():
    llm = ChatOllama(model="mistral")

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a helpful weather assistant. 
        If you need the current location, you MUST use the get_current_location tool.
        
        To answer questions about the current weather, you MUST use the get_current_weather tool.
        DO NOT make up weather information on your own.
        DO NOT write code.
        """,
            ),
            ("placeholder", "{messages}"),
        ]
    )

    agent_executor = create_react_agent(
        llm, [get_current_weather, get_current_location], prompt=prompt
    )
    query = f"What's the weather here?"
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
    weather_response = ask_current_weather()
    print("\nFinal Response:")
    print(weather_response)
