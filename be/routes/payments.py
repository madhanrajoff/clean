from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from models import Payments, PaymentUpdate

router = APIRouter()


@router.post("/payment-info", response_description="Create a new payment info", status_code=status.HTTP_201_CREATED,
             response_model=Payments)
def register_payment(request: Request, payment: Payments = Body(...)):
    info = jsonable_encoder(payment)
    payment = request.app.database["payments"].insert_one(info)
    created_info = request.app.database["payments"].find_one(
        {"_id": payment.inserted_id}
    )

    return created_info


@router.put("/payment-info", response_description="Update payments", response_model=Payments)
def payment_update(id: str, request: Request, payment: PaymentUpdate = Body(...)):
    info = {k: v for k, v in payment.dict().items() if v is not None}
    if len(info) >= 1:
        update_result = request.app.database["payments"].update_one(
            {"_id": id}, {"$set": info}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Payment with ID {id} not found")

    if (existing_info := request.app.database["payments"].find_one({"_id": id})) is not None:
        return existing_info

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Payment with ID {id} not found")
