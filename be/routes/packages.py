from fastapi import APIRouter, Request, HTTPException, status

from models import Packages

router = APIRouter()


@router.get("/", response_description="Get packages", response_model=Packages)
def list_package(request: Request):
    packages = list(request.app.database["packages"].find(limit=100))
    return packages


@router.get("/{id}/calculate-cost/{type}", response_description="Package cost")
def user_profile(id: str, type: str, request: Request):
    if (package := request.app.database["packages"].find_one({"_id": id})) is not None:
        # TODO: Incur charges based on type
        return package
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Package with ID {id} not found")


# TODO: For Admin to /Update, /Create, /Delete packages
