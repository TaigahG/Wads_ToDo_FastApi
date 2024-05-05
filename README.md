# Todo-FastAPI
| Endpoint | Method | Description | Body Request | Body Response | Error Response |
| -------- | ------ | ----------- | ------------ | ------------- | ----------- |
| /createTask | POST | Create a Task based on ID and Title. | `{ "id": {id}, "title": "{title}", "completed": false }` | `{ "id": {id}, "title": "{title}", "completed": false }` | `{"error": "Task not found"}` |
| /getTaskID/{task_id} | GET | Get a task based on ID. | - | `{ "id": {id}, "title": "{title}", "completed": {completed} }` | `{"error": "Task not found"}` |
| /deleteID/{task_id} | DELETE | Delete a task based on ID. | `{ "id": {id}, "title": "{title}", "completed": false }` | `{"message": "Task deleted successfully"}` | - |
| /deleteTitle/{title} | DELETE | Delete a task based on Title. | `{ "id": {id}, "title": "{title}", "completed": false }` | `{"message": "All tasks with title '{title}' deleted successfully"}`| - |
| /getAllTasks | GET | Get every task on available| `{ "id": {id}, "title": "{title}", "completed": false }` | `{ "id": {id}, "title": "{title}", "completed": false }` | - |
| /updateTask/{task_id} | PUT | Update a task by ID and request a new data | `{ "id": {id}, "title": "{title}", "completed": {completed} }` | `{"message": "Task updated successfully"}` | `{"error": "Task not found"}`|
| /completedTask/{task_id} | PUT | Complete a task based on ID | `{ "id": {id}, "title": "{title}", "completed": {completed} }` | `{"message": "Task updated successfully"}` | `{"error": "Task not found"}`|

