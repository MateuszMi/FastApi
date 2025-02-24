from fastapi.testclient import TestClient
from FastAPI import app

client = TestClient(app)

def test_create_book():
    response = client.post("/books/", json={
        "title": "The Speedway",
        "description": "The fastest bikes",
        "pages": 320
    })
    assert response.status_code == 200
    assert response.json()["title"] == "The Speedway"
    assert response.json()["description"] == "The fastest bikes"
    assert response.json()["pages"] == 320
    return response.json()["id"]

def test_get_all_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_book_by_id():
    book_id = test_create_book()
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["id"] == book_id

def test_update_book():
    book_id = test_create_book()
    response = client.put(f"/books/{book_id}", json={
        "title": "The Speedway",
        "description": "The fastest bikes",
        "pages": 400
    })
    assert response.status_code == 200
    assert response.json()["title"] == "The Speedway"

def test_partial_update_book():
    book_id = test_create_book()
    response = client.patch(f"/books/{book_id}", json={"pages": 450})
    assert response.status_code == 200
    assert response.json()["pages"] == 450

def test_delete_book():
    book_id = test_create_book()
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Book deleted successfully"
