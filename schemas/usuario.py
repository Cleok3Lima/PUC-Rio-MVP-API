from pydantic import BaseModel, Field, ConfigDict

class UsuarioSchema(BaseModel):
    username: str = Field(..., max_length=80)
    password: str = Field(..., min_length=6)

    model_config = ConfigDict(from_attributes=True)
