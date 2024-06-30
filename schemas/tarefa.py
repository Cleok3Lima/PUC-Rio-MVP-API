from pydantic import BaseModel, Field, field_serializer, ConfigDict
from typing import Optional
from datetime import datetime

class TarefaSchema(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str]
    due_date: Optional[datetime]
    completed: bool = Field(default=False)

    model_config = ConfigDict(from_attributes=True)

    @field_serializer('due_date')
    def serialize_due_date(self, value: Optional[datetime]) -> Optional[str]:
        return value.strftime('%d/%m/%Y') if value else None
