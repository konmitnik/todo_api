from pydantic import BaseModel

class Task(BaseModel):
    id: int | None = None
    title: str
    description: str | None = None
    is_completed: bool = False