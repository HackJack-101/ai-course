from langchain_core.prompts import MessagesPlaceholder
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent

from courses.course_4.response import get_current_location, get_system_message
from courses.course_4.weather_tool import get_current_weather


def ask_current_weather():
    llm = ChatOllama(model="llama3.1:8b", temperature=0.2)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                get_system_message(),
            ),
            MessagesPlaceholder("messages"),
        ]
    )

    agent_executor = create_react_agent(
        llm, [get_current_location, get_current_weather], prompt=prompt, debug=False
    )
    query = "What's the weather here?"
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
