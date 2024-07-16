from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

def majority(input):
    n = len(input)
    m = n // 2 + 1
    new_dict = {}
    for i in range(n):
        if input[i] in new_dict:
            new_dict[input[i]] += 1
        else:
            new_dict[input[i]] = 1

    for i, j in new_dict.items():
        if j >= m:
            return i
    return None

class InputModel(BaseModel):
    numbers: List[int]

@app.get("/majority/{num}")
def get_majority(num: str):
    result = majority(num)
    if result is None:
        raise HTTPException(status_code=404, detail="No majority element found")
    return {"majority_element": result}

@app.post("/majority")

def post_majority(input_model: InputModel):
    result = majority(input_model.numbers)
    if result is None:
        raise HTTPException(status_code=404, detail="No majority element found")
    return {"majority_element": result}
