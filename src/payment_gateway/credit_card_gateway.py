from decimal import Decimal

class CreditCardGateway:
    def process_payment(
        self,
        store_document: str,
        purchaser_document: str,
        purchase_value: Decimal,
    ) -> None:
        pass