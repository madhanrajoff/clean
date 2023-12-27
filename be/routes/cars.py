from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import Union, List, Dict

from models import Car_Type

router = APIRouter()


@router.get("/", response_description="Get all the master list of the cars", response_model=Union[Dict[str, int], dict])
def cars(request: Request):
    car_dict = {member.name: member.value for member in Car_Type}
    return car_dict


