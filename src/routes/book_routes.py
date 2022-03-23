from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from src.schemas.book_schemas import Response, RequestBook
from src.database.db import get_db
from src.crud import book_crud

router = APIRouter()

@router.post("/create")
async def create_book_service(request: RequestBook, db: Session = Depends(get_db)):
    book_crud.create_book(db, book=request.parameter)
    return Response(status="Ok", code="200",message="Book created successfully").dict(exclude_none=True)


@router.get("/")
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = book_crud.get_book(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=books)

@router.get("/{id}")
async def get_books(book_id:int, db: Session = Depends(get_db)):
    book = book_crud.get_book_by_id(db, book_id=book_id)
    if book is None:
        return Response(code="404", message="Book not found")
    return Response(status="Ok", code="200", message="Success fetch data by id", result=book)


@router.put("/update")
async def update_book(request: RequestBook, db: Session = Depends(get_db)):
    book = book_crud.update_book(db, book_id=request.parameter.id,
                            title=request.parameter.title, description=request.parameter.description)
    return Response(status="Ok", code="200", message="Success update data", result=book)


@router.delete("/delete")
async def delete_book(request: RequestBook,  db: Session = Depends(get_db)):
    book_crud.remove_book(db, book_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)