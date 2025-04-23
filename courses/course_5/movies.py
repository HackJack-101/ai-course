import sys

from langchain_core.prompts import MessagesPlaceholder
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent

from courses.course_5.response import get_system_message, get_movie_data


def ask_about_movies(user_message: str):
    llm = ChatOllama(model="llama3.1:8b")
    print(f"Question asked: {user_message}")

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
        llm, [get_movie_data], prompt=prompt, debug=False
    )
    messages = agent_executor.invoke(
        {
            "messages": [
                ("human", user_message),
            ]
        }
    )
    # Take the last message
    output = messages["messages"][-1].content

    return output


def main():
    if len(sys.argv) < 2:
        print("Please provide a movie question as argument")
        sys.exit(1)

    question = sys.argv[1]
    movie_response = ask_about_movies(question)
    print("\nFinal Response:")
    print(movie_response)
