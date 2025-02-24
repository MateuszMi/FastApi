from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import Optional
import uuid

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

class Book(Base):
    __tablename__ = "books"
    id = Column(String, primary_key=True, index=True, unique=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    pages = Column(Integer, index=True)

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    pages: Optional[int] = None

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=dict)
def create_book(title: str, description: str, pages: int, db: Session = Depends(get_db)):
    book = Book(id=str(uuid.uuid4()), title=title, description=description, pages=pages)
    db.add(book)
    db.commit()
    db.refresh(book)
    return {"id": book.id, "title": book.title, "description": book.description, "pages": book.pages}

@app.get("/books/", response_model=list)
def get_all_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return [{"id": book.id, "title": book.title, "description": book.description, "pages": book.pages} for book in books]

@app.get("/books/{book_id}", response_model=dict)
def read_book(book_id: str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"id": book.id, "title": book.title, "description": book.description, "pages": book.pages}

@app.get("/books/title/{book_title}", response_model=dict)
def read_book_by_title(book_title: str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.title == book_title).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"id": book.id, "title": book.title, "description": book.description, "pages": book.pages}

@app.put("/books/{book_id}", response_model=dict)
def update_book(book_id: str, title: str, description: str, pages: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = title
    book.description = description
    book.pages = pages
    db.commit()
    db.refresh(book)
    return {"id": book.id, "title": book.title, "description": book.description, "pages": book.pages}

@app.patch("/books/{book_id}", response_model=dict)
def patch_book(book_id: str, book_update: BookUpdate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    if book_update.title is not None:
        book.title = book_update.title
    if book_update.description is not None:
        book.description = book_update.description
    if book_update.pages is not None:
        book.pages = book_update.pages
    db.commit()
    db.refresh(book)
    return {"id": book.id, "title": book.title, "description": book.description, "pages": book.pages}

@app.delete("/books/{book_id}")
def delete_book(book_id: str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted successfully"}
