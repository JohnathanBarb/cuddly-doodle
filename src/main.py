import logging
from decimal import Decimal

from fastapi import FastAPI, responses
from pydantic import BaseModel

from src.use_case.payment_process import (
    PaymentProcessDTO,
    PaymentProcessError,
    PaymentProcessUseCase,
)

logger = logging.getLogger(__name__)
app = FastAPI()


class ProcessCashbackPayload(BaseModel):
    store_document: str
    purchaser_document: str
    purchase_value: Decimal
    payment_method: str


@app.post("/api/payment/process")
def payment_process(payload: ProcessCashbackPayload):
    use_case = PaymentProcessUseCase()

    dto = PaymentProcessDTO(
        store_document=payload.store_document,
        purchase_value=payload.purchase_value,
        payment_method=payload.payment_method,
        purchaser_document=payload.purchaser_document,
    )

    try:
        result = use_case.execute(dto)

        return responses.JSONResponse(
            content={"message": result},
            status_code=200,
        )
    except PaymentProcessError as e:
        logger.exception("Erro esperado")
        return responses.JSONResponse(status_code=400, content={"message": str(e)})

    except Exception as e:
        logger.exception("Erro inesperado")
        return responses.JSONResponse(status_code=500, content={"message": str(e)})
