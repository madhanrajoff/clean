from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import Optional, List

from models import User, UserUpdate, UserCar, UserCarUpdate

router = APIRouter()


@router.post("/", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=User)
def register_user(request: Request, user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id}
    )

    return created_user


@router.get("/profile/{id}", response_description="Get user profile by id", response_model=User)
def user_profile(id: str, request: Request):
    if (user := request.app.database["users"].find_one({"_id": id})) is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")


@router.put("/profile/{id}", response_description="Update a user", response_model=User)
def profile_update(id: str, request: Request,
                   user: UserUpdate = Body(..., example=UserUpdate.Config.json_schema_extra)):
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


@router.post("/{id}/cars", response_description="Create a new car for the given user",
             status_code=status.HTTP_201_CREATED, response_model=UserCar)
def register_user_car(id: str, request: Request, user_car: UserCar = Body(...)):
    user_car = jsonable_encoder(user_car)
    print("register----", user_car)
    new_car = request.app.database["car"].insert_one(user_car["car"])
    user_car = {
        **user_car,
        "user_id": id,
        "car": request.app.database["car"].find_one({"_id": new_car.inserted_id})}
    new_user_car = request.app.database["user_car"].insert_one(user_car)
    created_user_car = request.app.database["user_car"].find_one(
        {"_id": new_user_car.inserted_id}
    )

    return created_user_car


@router.get("/{id}/cars", response_description="Get all the car belongs to the particular user",
            response_model=List[UserCar])
def user_car(id: str, request: Request):
    if (user_cars_cursor := request.app.database["user_car"].find({"user_id": id})) is not None:
        return [user_car for user_car in user_cars_cursor]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")


@router.patch("/{id}/cars/{car_id}", response_description="Update a user", response_model=UserCarUpdate)
def user_car_update(id: str, car_id: str, request: Request,
                   user_car_update: UserCarUpdate = Body(..., example=UserCarUpdate.Config.json_schema_extra)):
    user_car = {k: v for k, v in user_car_update.dict().items() if v is not None}
    if len(user_car) >= 1:
        user_car["car"].pop("id")
        _update_car = request.app.database["car"].update_one(
            {"_id": car_id}, {"$set": user_car["car"]}
        )
        if (existing_car := request.app.database["car"].find_one({"_id": car_id})) is not None:
            user_car["car"] = existing_car
            _update_result = request.app.database["user_car"].update_one(
                {"_id": id}, {"$set": user_car}
            )

    if (existing_user_car := request.app.database["user_car"].find_one({"_id": id})) is not None:
        return existing_user_car

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")


# @router.delete("/delete-account/{id}", response_description="Delete my user")
# def delete_account(id: str, request: Request, response: Response):
#     status_update = request.app.database["users"].update_one(
#             {"_id": id}, {"$set": {"status": UserStatus.INACTIVE.value}}
#         )
#
#     # TODO: Check if status_update value by debugger
#     if status_update is not None:
#         response.status_code = status.HTTP_204_NO_CONTENT
#         return response
#
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")
