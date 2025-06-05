from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    score: int = 0
    
    class Config:
        schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "secret",
                "score": 100
            }
        }