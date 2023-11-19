from datetime import datetime
import uuid
from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum


class UserStatus(Enum):
    ACTIVE = 1
    INACTIVE = 0


class Car(BaseModel):
    make: str
    model: str
    number: str


class ReferralActivity(BaseModel):
    mode: str = Field(...)  # TODO: Enum, ex: Mode - Subscription, Referral, etc...
    reference_id: str = Field(...)  # Payment id


class ReferralPoints(BaseModel):
    date: datetime = Field(...)
    points: int = Field(...)
    activity: List[ReferralActivity] = []


class Users(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str = Field(...)
    contact: int = Field(...)
    address: str = Field(...)
    status: UserStatus
    email: Optional[str]
    cars: Optional[List[Car]]
    referral: Optional[int]
    referral_points: Optional[List[ReferralPoints]]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "username": "Don Quixote",
                "contact": 0000000000,
                "address": "...",
                "email": "test@gmail.com",
                "cars": [
                    {"make": "Toyota", "model": "Camry", "number": "1234"},
                    {"make": "Ford", "model": "Focus", "number": "5678"}
                ]
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
    price: int = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Don Quixote",
                "price": 600
            }
        }


class Apartments(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    address: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "Don Quixote",
                "name": "Don Quixote",
                "address": "..."
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
