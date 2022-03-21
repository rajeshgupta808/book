from sqlalchemy.orm import Session
from src.models.book_models import Book
from src.schemas.book_schemas import BookSchema


def get_book(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, book: BookSchema):
    book = Book(id=book.id,title=book.title, description=book.description)

    db.add(book)
    db.commit()
    db.rollback()
    db.refresh(book)
    return book


def remove_book(db: Session, book_id: int):
    book = get_book_by_id(db=db, book_id=book_id)
    db.delete(book)
    db.commit()


def update_book(db: Session, book_id: int, title: str, description: str):
    book = get_book_by_id(db=db, book_id=book_id)

    book.title = title
    book.description = description

    db.commit()
    db.refresh(book)
    return book