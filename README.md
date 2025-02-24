# FastAPI CRUD App – Books API

## Start App

### Install the required libraries:
    pip install fastapi uvicorn sqlalchemy pydantic

### Run the server:
    uvicorn FastAPI:app --reload

### Open the API documentation in your browser:
Swagger UI: http://127.0.0.1:8000/docs

## Endpoints
### POST /books/

Example Request:
```
{
  "title": "The Speedway",
  "description": "The fastest bikes",
  "pages": 100
}
```
Example Response:
```
{
  "id": "350e1400-e29b-51d4-a716-446655440002",
  "title": "The Speedway",
  "description": "The fastest bikes",
  "pages": 100
}
```

### GET /books/
Returns a list of all books in the database.
Example Response:
```
[
  {
  "id": "350e1400-e29b-51d4-a716-446655440002",
  "title": "The Speedway",
  "description": "The fastest bikes",
  "pages": 100
  }
]
```

### GET /books/{book_id}
Returns the details of a book based on the unique ID.
Example Response:
```
  {
  "id": "350e1400-e29b-51d4-a716-446655440002",
  "title": "The Speedway",
  "description": "The fastest bikes",
  "pages": 100
  }
```

### GET /books/title/{book_title}
Returns a book with the given title.
Example Response:
```
  {
  "id": "350e1400-e29b-51d4-a716-446655440002",
  "title": "The Speedway",
  "description": "The fastest bikes",
  "pages": 100
  }
```

### PUT /books/{book_id}
Updates all fields of a book.

Example Request:
```
  {
  "title": "The Speedway 2",
  "description": "The fastest bikes",
  "pages": 120
  }
```
Example Response:
```
  {
  "id": "350e1400-e29b-51d4-a716-446655440002",
  "title": "The Speedway 2",
  "description": "The fastest bikes",
  "pages": 120
  }
```

### PATCH /books/{book_id}
Allows changes to only selected fields of a book.

Example Request:
```
  {
  "title": "The Speedway 5",
  }
```
Example Response:
```
  {
  "id": "350e1400-e29b-51d4-a716-446655440002",
  "title": "The Speedway 5",
  "description": "The fastest bikes",
  "pages": 120
  }
```

### DELETE /books/{book_id}
Deletes a book from the database.

 Example Response:
```
{
  "detail": "Book deleted successfully"
}
```

## Start test

### Install the required libraries:
        pip install pytest httpx

### Run the tests:
    pytest tests.py
