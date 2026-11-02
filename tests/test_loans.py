import pytest

def loan_payload(
        equipment_id=1,
        borrower_name="Mike",
        loan_days=7,
        purpose="Nun ya",
        #status="PENDING",
):
    return {
        "equipment_id": equipment_id,
        "name": borrower_name,
        "loan_days": loan_days,
        "purpose": purpose,
        #"status": status,
    }

def test_create_loan_returns_201(client):
    response=client.post("/api/loans", json=loan_payload())
    assert response.status_code == 201
    data = response.json()
    assert data["name" ] == "Mike"

def test_duplicate_loan_returns_409(client):
   client.post("/api/loans", json=loan_payload())
   response=client.post("/api/loans", json=loan_payload())
   assert response.status_code == 409
   assert "already exists" in response.json()["detail"].lower()

def test_deleted_user_returns_404(client):
    created=client.post("/api/loans",json=loan_payload()).json()
    loan_id=created["id"]
    response=client.delete(f"/api/loans/{loan_id}")
    assert response.status_code == 204
    get = client.get("/api/loans/999")
    assert get.status_code == 404