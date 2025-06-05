from pydantic import BaseModel


class Client(BaseModel):
    id: str
    connected: bool = False
    last_activity: str = ""
