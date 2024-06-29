from pydantic import BaseModel, Field

class UsuarioSchema(BaseModel):
    username: str = Field(..., max_length=80)
    password: str = Field(..., min_length=6)
