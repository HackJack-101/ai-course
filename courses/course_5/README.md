# Movies database

## Requirements

- a neo4j database

## Installation

- Open the [console](http://localhost:7474/browser/)
- `CREATE DATABASE aicourse`
- `:use aicourse`
- `:play movies`
- Execute the query in page 2
- Your database is now ready

## Exercice

- Write a file named `response.py` which contains :
  - a tool named `get_movie_data`
  - a class `MovieCypher` as argument of the tool
  - a function named `get_system_message()`
- You have to call the neo4j database to have the answer to the user's question