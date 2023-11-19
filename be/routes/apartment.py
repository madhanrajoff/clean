from fastapi import APIRouter, Request
from models import Apartments

router = APIRouter()


@router.get("/", response_description="List apartments", response_model=Apartments)
def list_apartment(request: Request):
    apartment = list(request.app.database["apartments"].find(limit=100))
    return apartment


# TODO: For Admin to /Update, /Create, /Delete appartments
