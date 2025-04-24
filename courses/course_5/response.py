from typing import Dict
from langchain_core.tools import tool
from pydantic import Field, BaseModel

from courses.course_5.neo4j_tool import run_cypher_query


class MovieCypher(BaseModel):
    cypher: str = Field(description="The cypher query to execute to get movie data")


def get_system_message() -> str:
    return """You are a movie database assistant. The user will ask you something about movies, actors and directors. 
        To answer it, you MUST use the get_movie_data tool.
        
        The neo4j relations are :
        - `ACTED_IN` between `Person` and `Movie` nodes when Person is an actor: `(p:Person)-[:ACTED_IN]->(m:Movie)`
        - `DIRECTED` between `Person` and `Movies` nodes when Person is an director: `(p:Person)-[:DIRECTED]->(m:Movie)`
        Person nodes have a name attribute.
        
        DO NOT make up information on your own.
        """


@tool(
    name_or_callable="get_movie_data",
    description="Get movie data from a Neo4j cypher",
    return_direct=False,
    args_schema=MovieCypher,
)
def get_movie_data(cypher: str) -> Dict:
    try:
        print(f"Calling neo4j with cypher: {cypher}")
        results = run_cypher_query(cypher)

        return {"results": results}

    except Exception as e:
        return {
            "error": f"Failed to get data movie: {str(e)}",
        }
