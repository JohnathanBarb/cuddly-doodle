from decimal import Decimal
from dataclasses import dataclass

from src.payment_gateway.credit_card_gateway import CreditCardGateway
from src.payment_gateway.debit_card_gateway import DebitCardGateway



@dataclass
class PaymentProcessDTO:
    store_document: str
    purchaser_document: str
    purchase_value: Decimal
    payment_method: str


class PaymentProcessError(Exception):
    pass


class PaymentProcessUseCase:
    def __init__(self) -> None:
        self.credit_card_gateway = CreditCardGateway()
        self.debit_card_gateway = DebitCardGateway()

    def execute(self, payment_process_dto: PaymentProcessDTO) -> None:
   
        if payment_process_dto.payment_method == "credit_card":
            self.credit_card_gateway.process_payment(
                store_document=payment_process_dto.store_document,
                purchaser_document=payment_process_dto.purchaser_document,
                purchase_value=payment_process_dto.purchase_value
            )
            return
        

        if payment_process_dto.payment_method == "debit_card":
            self.debit_card_gateway.process_payment(
                store_document=payment_process_dto.store_document,
                purchaser_document=payment_process_dto.purchaser_document,
                purchase_value=payment_process_dto.purchase_value
            )
            return
    
        raise PaymentProcessError("Unsupported payment method")
