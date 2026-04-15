from fastapi import APIRouter, Depends, HTTPException
from models.task import Task

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)

fake_database = []

def pagination_parameters(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@router.get("")
def get_tasks(pagination: dict = Depends(pagination_parameters)):
    skip = pagination["skip"]
    limit = pagination["limit"]

    return fake_database[skip:skip+limit]

@router.post("")
def create_task(task: Task):
    new_task = task.dict()
    new_task["id"] = len(fake_database) + 1

    fake_database.append(new_task)
    return new_task

@router.get("/{task_id}")
def get_task(task_id: int):
    for _, t in enumerate(fake_database):
        if not t["id"] == task_id:
            continue

        return t
    
    raise HTTPException(status_code=404, detail="Задача не найдена")


@router.put("/{task_id}")
def update_task(task_id: int, task: Task):
    for idx, t in enumerate(fake_database):
        if not t["id"] == task_id:
            continue

        updated_task = task.dict()
        updated_task["id"] = task_id
        fake_database[idx] = updated_task
        return updated_task
    
    raise HTTPException(status_code=404, detail="Задача не найдена")

@router.delete("/{task_id}")
def delete_task(task_id: int):
    for idx, t in enumerate(fake_database):
        if not t["id"] == task_id:
            continue

        del fake_database[idx]
        return {"meassage": "Задача успешно удалена"}
    
    raise HTTPException(status_code=404, detail="Задача не найдена")