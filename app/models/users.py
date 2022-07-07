from typing import Optional
from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    email: Optional[str]
    fullname: Optional[str]
    class Config:
        schema_extra = {
            "example":{
                "email": "xyz@xyz.com",
                "fullname": "Albert Einstein"
            }
        }


def ResponseModel(data, message):
    return {
        "data":[data],
        "code":200,
    }

def ErrorResponseModel(error, code):
    return {
        "error": error,
        "code": code,
    }