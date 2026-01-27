from fastapi import FastAPI, responses
from pydantic import BaseModel
from decimal import Decimal
from src.use_case.payment_process import PaymentProcessDTO, PaymentProcessUseCase


app = FastAPI()

class ProcessCashbackPayload(BaseModel):
    store_document: str
    
    purchaser_document: str
    purchase_value: Decimal

    payment_method: str




@app.post("/api/payment/process")
def payment_process(
    payload: ProcessCashbackPayload
):

    use_case = PaymentProcessUseCase()

    dto = PaymentProcessDTO(
        store_document=payload.store_document,
        purchase_value=payload.purchase_value,
        payment_method=payload.payment_method,
        purchaser_document=payload.purchaser_document,
    )

    try:
        use_case.execute(dto)
    

        return responses.Response(status_code=204)
    except Exception as e:
        return responses.JSONResponse(
            status_code=400,
            content={"message": str(e)}
        )
