# Reasoning

Some LLM can explain the reasoning behind their answer.
In this demo, we will test some models resolve a math problem (dice) and a physics problem.

## Dice problem

- deepseek-r1:8b ✅
- mistral:latest ❌
- phi4-mini ✅
- granite3.3:8b ❌

### Physics problem

- deepseek-r1:8b 💀
- mistral:latest ❌
- phi4-mini 💀
- granite3.3:8b ❌

## Exercice: Algebraic expression

We will try to solve an algebraic expression when a LLM cannot do it.

- Write `response.py` to fix the test written in `test_fix_math_problem.py`
- You have to call a LLM and the model used must be `mistral:latest`
- You can use multiple functions to solve the expression (this is the case in the test)

