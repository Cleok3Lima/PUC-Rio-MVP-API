from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Especifica a apresentação de uma mensagem de erro.
    """
    mesage: str
