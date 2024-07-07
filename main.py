from fastapi import FastAPI
from todo_model import Todo

app = FastAPI()

todos = []


@app.get("/")
async def root():
    return "Welcome to my TODO"


# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}


# Get single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return f"No Todo of ID: {todo_id} found!"


# Create a todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return "Todo has been added!"


# Update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_item: str):
    for todo in todos:
        if todo.id == todo_id:
            todo.item = todo_item
            return {"todo": todo}
    return f"No Todo of ID: {todo_id} found!"


# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return "Todo has been deleted!"
    return f"No Todo of ID: {todo_id} found!"
