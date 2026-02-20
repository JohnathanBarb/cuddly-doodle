from dataclasses import dataclass
from decimal import Decimal


@dataclass
class PaymentProcessDTO:
    store_document: str
    purchaser_document: str
    purchase_value: Decimal
    payment_method: str


class PaymentProcessError(Exception):
    pass


def process_credit_card_payment(
    purchaser_document: str,
    purchase_value: Decimal,
    store_document: str,
) -> str:
    # Essa função faz o processamento do pagamento, utilizando cartão de credito
    return f"A Cielo processou o pagamento para a loja {store_document}"


def process_debit_card_payment(
    purchaser_document: str,
    purchase_value: Decimal,
    store_document: str,
) -> str:
    # Essa função faz o processamento do pagamento, utilizando cartão de débito
    return f"A Cielo processou uma compra no cartão de débito do cliente {purchaser_document}"


class PaymentProcessUseCase:
    def execute(self, payment_process_dto: PaymentProcessDTO) -> str:
        if payment_process_dto.payment_method == "credit_card":
            return process_credit_card_payment(
                purchaser_document=payment_process_dto.purchaser_document,
                purchase_value=payment_process_dto.purchase_value,
                store_document=payment_process_dto.store_document,
            )

        if payment_process_dto.payment_method == "debit_card":
            return process_debit_card_payment(
                purchaser_document=payment_process_dto.purchaser_document,
                purchase_value=payment_process_dto.purchase_value,
                store_document=payment_process_dto.store_document,
            )

        raise PaymentProcessError("Método de pagamento não suportado")
