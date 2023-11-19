import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Users(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str = Field(...)
    contact: str = Field(...)
    address: str = Field(...)
    email: Optional[str]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "username": "Don Quixote",
                "contact": "0000000000",
                "address": "...",
                "email": "test@gmail.com"
            }
        }


class UserUpdate(BaseModel):
    username: Optional[str]
    address: Optional[str]
    email: Optional[str]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "username": "Don Quixote",
                "address": "...",
                "email": "test@gmail.com"
            }
        }


class Packages(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Don Quixote"
            }
        }


class Slots(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    morning: bool = Field(...)
    afternoon: bool = Field(...)
    evening: bool = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "morning": False,
                "afternoon": True,
                "evening": False
            }
        }


class Subscriptions(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    package: Packages
    user: Users
    slots: Slots

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "package": {"_id": "package_id", "name": "Package Name"},
                "user": {"_id": "user_id", "username": "User Name", "contact": "0000000000", "address": "User Address",
                         "email": "User Email"},
                "slots": {"_id": "slots_id", "morning": False, "afternoon": True, "evening": False}
            }
        }
