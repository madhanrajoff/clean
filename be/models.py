from datetime import datetime
import uuid
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum


class Car_Type(Enum):
    Mini_Hatchbak = 0
    Hatchback = 1
    Premium_Hatchback = 2
    Sedan = 3
    Premium_Sedan = 4
    SUV = 5
    Premium_SUV = 6
    Luxury = 7


class Apartment(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    address: str = Field(...)
    is_active: bool = Field(...)
    created_on: datetime = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "...",
                "name": "...",
                "address": "...",
                "is_active": True,
                "created_on": datetime.now(),
            }
        }


class Car(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    make: str = Field(...)
    name: str = Field(...)
    model: int = Field(...)
    type: Car_Type

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "...",
                "make": "...",
                "name": "...",
                "model": "...",
                "type": Car_Type.Mini_Hatchbak.name,
            }
        }


class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    mobile_number: int = Field(...)
    firstname: Optional[str] = Field(...)
    lastname: Optional[str] = Field(...)
    email: Optional[str]
    apartment: Optional[Apartment] = Field(...)
    referred_by: Optional[str] = Field(...)
    total_reward_points: int
    is_active: bool = Field(...)
    created_on: datetime = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "...",
                "mobile_number": 000,
                "firstname": "...",
                "lastname": "...",
                "email": "...",
                "apartment": {"field1": "...", "field2": "..."},  # Example data for Apartment
                "referred_by": "...",
                "total_reward_points": 0,
                "is_active": True,
                "created_on": datetime.now(),
            }
        }


class UserCar:
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user: User
    car: Car
    color: str = Field(...)
    number: str = Field(...)
    is_active: bool = Field(...)
    created_on: datetime = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "...",
                "user": {"field1": "...", "field2": "..."},  # Example data for User
                "car": {"field1": "...", "field2": "..."},  # Example data for Car
                "color": "...",
                "number": "...",
                "is_active": True,
                "created_on": datetime.now(),
            }
        }


class Service(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    is_active: bool = Field(...)
    created_on: datetime = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "...",
                "name": "...",
                "is_active": True,
                "created_on": datetime.now(),
            }
        }


class Package(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    services: List[Service] = []
    awarded_points: int
    is_active: bool = Field(...)
    created_on: datetime = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "...",
                "name": "...",
                "description": "...",
                "services": [{"field1": "...", "field2": "..."}],  # Example data for Services
                "awarded_points": 0,
                "is_active": True,
                "created_on": datetime.now(),
            }
        }


class Subscription_Status(Enum):
    Inactive = 0
    Active = 1
    Suspended = 2
    Expired = 3


class Payment_Status(Enum):
    Intiated = 0
    InProgress = 1
    Succeeded = 2
    Failed = 3


class Payment(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    amount: int
    status: Payment_Status
    created_on: datetime = Field(...)
    updated_on: datetime = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "...",
                "amount": 699,
                "status": Payment_Status.Intiated.name,
                "created_on": datetime.now(),
                "updated_on": datetime.now(),
            }
        }


class Subscription(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_car: UserCar
    status: Subscription_Status
    payment: Payment
    created_on: datetime = Field(...)
    expires_on: datetime = Field(...)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed=True
        json_schema_extra = {
            "example": {
                "_id": "...",
                "user_car": {"field1": "...", "field2": "..."},  # Example data for UserCar
                "status": Subscription_Status.Inactive.name,
                "payment": {"field1": "...", "field2": "..."},  # Example data for Payment,
                "created_on": datetime.now(),
                "expires_on": datetime.now(),
            }
        }


class Activity(Enum):
    Referral = 0
    Subscription = 1
    Spend = 2


class PointsTracker(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user: User
    activity: Activity
    reference_id: str  # Id of Payment for Spend, Id of Subscription for Subscription, Id of User for Referral
    points: int
    created_on: datetime = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "...",
                "user": {"field1": "...", "field2": "..."},  # Example data for User
                "activity": Activity.Referral.name,
                "reference_id": "...",
                "points": 10,
                "created_on": datetime.now(),
            }
        }
