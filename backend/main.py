from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)



@app.get("/")
async def root():
    return {"message": "Hello World"}


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    completed: bool = False  


task_id_count = 0
tasks = {}

@app.post("/createTask")
def create_task(task: Task):
    global task_id_count
    task_id = task_id_count
    task.id = task_id
    tasks[task_id] = task
    task_id_count += 1 
    return task

@app.get("/getTaskID/{task_id}")
def get_task_by_id(task_id: int):
    if task_id in tasks:
        return tasks[task_id]
    else:
        return {"error": "Task not found"}





@app.delete("/deleteID/{task_id}")
def delete_task_by_id(task_id: int):
    if task_id in tasks:
        del tasks[task_id]
        return {"message": "Task deleted successfully"}
    else:
        return {"error": "Task not found"}


@app.delete("/deleteTitle/{title}")
def delete_task_by_title(title: str):
    tasks_to_delete = [task_id for task_id, task in tasks.items() if task.title == title]
    if tasks_to_delete:
        for task_id in tasks_to_delete:
            del tasks[task_id]
        return {"message": f"All tasks with title '{title}' deleted successfully"}
    else:
        return {"error": f"No tasks found with title '{title}'"}


@app.get("/getAllTasks")
def get_all_tasks():
    return list(tasks.values())


@app.put("/updateTask/{task_id}")
def update_task(task_id: int, updated_task: Task):
    if task_id in tasks:
        tasks[task_id] = updated_task
        return {"message": "Task updated successfully"}
    else:
        return {"error": "Task not found"}
    
@app.put("/completedTask/{task_id}")
def completed_task(task_id: int):
    if task_id in tasks:
        tasks[task_id].completed = True
        return {"message": "Task completed successfully"}
    else:
        return {"error": "Task not found"}