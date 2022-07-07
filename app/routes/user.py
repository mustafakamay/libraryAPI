from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.database.users import (
    userDetail,
    retrieve_users,
    userAdd,
    userUpdate,
    userDelete
)

from app.models.users import (
    UserSchema,
    ResponseModel,
    ErrorResponseModel
)

router = APIRouter()
@router.get("/", response_description="Users retrieved")
async def get_users():
    users = retrieve_users()
    if users:
        return ResponseModel(users, "All user list")
    return ResponseModel(users, "List is empty")

@router.post("/add")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = userAdd(user)
    return ResponseModel(new_user, "User added")

@router.get("/detail/{id}", response_description="User data retrieved")
async def get_user_data(id):
    user = userDetail(id)
    if user:
        return ResponseModel(user, "User detail successfuly")
    return ErrorResponseModel("User does not exist", 404)

@router.put("/update/{id}")
async def update_user_data(id, req: UserSchema = Body(...)):
    req = { k: v for k, v in req.dict().items() if v is not None }
    updated_user = userUpdate(id, req)
    if updated_user:
        return ResponseModel(updated_user, "User updated.")
    return ErrorResponseModel("User does not exist", 404)

@router.delete("/delete/{id}", response_description="User data deleted from database")
async def delete_user_data(id: str):
    deleted_user = userDelete(id)
    if deleted_user:
        return ResponseModel(deleted_user, "User deleted successfully.")
    return ErrorResponseModel("User does not exist", 404)

