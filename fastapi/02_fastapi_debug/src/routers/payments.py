from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from src.models import Payment
from src.payment_processor import process_payment

payments_router = APIRouter(prefix="/api")


@payments_router.post("/payments")
async def make_payment(params: Payment) -> JSONResponse:
    print(params)
    if params.customer_id is None:
        return HTTPException(
            status_code=400, content={"message": "Customer ID is required"}
        )

    payment_amount = process_payment(amount=params.amount, discount_percent=15)

    return {"message": f"Payment has been made: ${payment_amount}"}
