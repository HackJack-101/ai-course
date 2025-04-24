# Logic Detection in text

## Exercice

1. Create a file named `response.py`

2. Write the function `get_system_message()`
```python
def get_system_message() -> dict:
    return {"role": "system","content": "You are a world class AI."}
```

3. Write the class `Character` with pydantic

Example of a pydantic class :
```python
from datetime import datetime
from pydantic import BaseModel, PositiveInt

class User(BaseModel):
    id: int  
    name: str = 'John Doe'  
    signup_ts: datetime | None  
    tastes: dict[str, PositiveInt]  
```