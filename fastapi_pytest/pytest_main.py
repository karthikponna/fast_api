from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Todo(BaseModel):
    name: str
    completed: bool

# Mock database
todos = {}

@app.get("/", response_model=List[Todo])
async def read_todos():
    return list(todos.values())

@app.post("/", response_model=Todo)
async def create_todo(todo:Todo):
    todo_id = str(len(todos) +1)
    todos[todo_id] = todo

@app.get("/{todo_id}", response_model=Todo)
async def read_todo(todo_id: str):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="To do not found")
    return todo

@app.post("/{todo_id}", response_model=Todo)
async def update_todo(todo_id: str, update_todo: Todo):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="To do not found")
    todos[todo_id] = update_todo
    return update_todo

@app.delete("/{todo_id}", response_model=Todo)
async def delete_todo(todo_id: str):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="To do not found")
    
    del todos[todo_id]
    return todo