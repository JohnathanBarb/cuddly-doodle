import pytest

from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_payment_process_credit_card(client):
    payload = {
        "store_document": "12345678901234",
        "purchaser_document": "98765432100",
        "purchase_value": "150.75",
        "payment_method": "credit_card",
    }

    response = client.post("/api/payment/process", json=payload)

    assert response.status_code == 200
    assert response.json() == {"message": "Payment processed via credit card"}


def test_payment_process_debit_card(client):
    payload = {
        "store_document": "12345678901234",
        "purchaser_document": "98765432100",
        "purchase_value": "150.75",
        "payment_method": "debit_card",
    }

    response = client.post("/api/payment/process", json=payload)

    assert response.status_code == 200
    assert response.json() == {"message": "Payment processed via debit card"}


def test_payment_process_unsupported_payment_method(client):
    payload = {
        "store_document": "12345678901234",
        "purchaser_document": "98765432100",
        "purchase_value": "150.75",
        "payment_method": "paypal",
    }

    response = client.post("/api/payment/process", json=payload)

    assert response.status_code == 400
    assert response.json() == {"message": "Unsupported payment method"}
