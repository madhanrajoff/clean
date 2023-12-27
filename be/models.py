from datetime import datetime
import uuid
from typing import Optional, List, Dict, Any, Type
from pydantic import BaseModel, Field, create_model
from enum import Enum


def create_update_model(base_model: Type[BaseModel], exclude_fields: list[str]) -> Type[BaseModel]:
    # Get all fields from the base model except those in exclude_fields
    fields = {
        name: (field, ...) for name, field in base_model.__annotations__.items() if name not in exclude_fields
    }

    # Check if the Config class exists in the base_model
    config_class = getattr(base_model, 'Config', None)

    # Create the update model
    update_model = create_model(
        base_model.__name__ + "Update",
        **fields
    )

    # Set json_schema_extra directly on the Config of update_model if Config exists
    if config_class:
        update_model.Config = config_class
        attr = getattr(config_class, 'json_schema_extra', {})
        update_model.Config.json_schema_extra = {name: v for name, v in attr['example'].items() if
                                                 name not in exclude_fields}

    return update_model


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
    created_on: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "name": "...",
                "address": "...",
                "is_active": True,
            }
        }


class Car(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    make: str = Field(...)
    name: str = Field(...)
    model: int = Field(...)
    type: int = Car_Type

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "make": "...",
                "name": "...",
                "model": 2016,
                "type": Car_Type.Mini_Hatchbak.value,
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
    created_on: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "mobile_number": 1234567890,
                "firstname": "...",
                "lastname": "...",
                "email": "...",
                "apartment": {
                    "name": "...",
                    "address": "...",
                    "is_active": True,
                },
                "referred_by": "...",
                "total_reward_points": 0,
                "is_active": True,
            }
        }


# Create an user update model excluding certain key fields (e.g., 'mobile_number')
UserUpdate = create_update_model(User, exclude_fields=["id", "mobile_number"])


class UserCar(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user: Optional[str] = Field(default=None, alias="user_id")
    car: Car
    color: str
    number: str
    is_active: Optional[bool] = Field(default_factory=lambda: True)
    created_on: Optional[datetime] = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "car": {"make": "...",
                        "name": "...",
                        "model": 2016,
                        "type": Car_Type.Mini_Hatchbak.value, },  # Example data for Car
                "color": "...",
                "number": "...",
            }
        }


UserCarUpdate = create_update_model(UserCar, exclude_fields=["id", "user", "is_active", "created_on"])


class Service(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    is_active: bool = Field(...)
    created_on: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "name": "...",
                "is_active": True,
            }
        }


class Package(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    services: List[Service] = []
    awarded_points: int
    is_active: bool = Field(...)
    created_on: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "name": "...",
                "description": "...",
                "services": [{"field1": "...", "field2": "..."}],  # Example data for Services
                "awarded_points": 0,
                "is_active": True,
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
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "amount": 699,
                "status": Payment_Status.Intiated.name,
            }
        }


class Subscription(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_car: UserCar
    status: Subscription_Status
    payment: Payment
    created_on: datetime = Field(default_factory=datetime.now)
    expires_on: datetime = Field(...)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "user_car": {"field1": "...", "field2": "..."},  # Example data for UserCar
                "status": Subscription_Status.Inactive.name,
                "payment": {"field1": "...", "field2": "..."},  # Example data for Payment,
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
    created_on: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "user": {"field1": "...", "field2": "..."},  # Example data for User
                "activity": Activity.Referral.name,
                "reference_id": "...",
                "points": 10,
            }
        }
