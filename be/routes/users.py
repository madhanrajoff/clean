from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from models import Users, UserUpdate, UserStatus

router = APIRouter()


@router.post("/register", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=Users)
def register_user(request: Request, user: Users = Body(...)):
    user = jsonable_encoder(user)
    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id}
    )

    return created_user


@router.get("/profile/{id}", response_description="Get user profile by id", response_model=Users)
def user_profile(id: str, request: Request):
    if (user := request.app.database["users"].find_one({"_id": id})) is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")


@router.put("/profile/{id}", response_description="Update a user", response_model=Users)
def profile_update(id: str, request: Request, user: UserUpdate = Body(...)):
    user = {k: v for k, v in user.dict().items() if v is not None}
    if len(user) >= 1:
        update_result = request.app.database["users"].update_one(
            {"_id": id}, {"$set": user}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")

    if (
        existing_user := request.app.database["users"].find_one({"_id": id})
    ) is not None:
        return existing_user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")


@router.delete("/delete-account/{id}", response_description="Delete my user")
def delete_account(id: str, request: Request, response: Response):
    status_update = request.app.database["users"].update_one(
            {"_id": id}, {"$set": {"status": UserStatus.INACTIVE.value}}
        )

    # TODO: Check if status_update value by debugger
    if status_update is not None:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")
