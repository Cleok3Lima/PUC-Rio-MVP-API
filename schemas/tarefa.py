from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TarefaSchema(BaseModel):
    title: str
    description: Optional[str]
    due_date: Optional[datetime]
    completed: bool = False
