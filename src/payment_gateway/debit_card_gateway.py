from decimal import Decimal

class DebitCardGateway:
    def process_payment(
        self,
        store_document: str,
        purchaser_document: str,
        purchase_value: Decimal,
    ) -> None:
        pass