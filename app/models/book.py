from typing import Optional
from pydantic import BaseModel, Field

class BookSchema(BaseModel):
    name: str = Field(...)
    author: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "The Speech",
                "author": "M.Kemal ATATÜRK"
            }
        }

def ResponseModel(data, message):
    return {
        "response":[data],
        "status":200,
    }

def ErrorResponseModel(error, code):
    return {
        "response": error,
        "status": code,
    }