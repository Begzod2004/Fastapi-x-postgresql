from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from .config import SessionLocal
from sqlalchemy.orm import Session
from .schemas import BookSchema, Request, Response, RequestBook, RequestBookUpdate, RequestBookCreate, RequestBookDelete
from . import crud


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get('/')
async def get(db:Session=Depends(get_db)):
  _book = crud.get_book(db, 0, 100)
  return Response(code=200, status='Ok', message='Success Fetch all data', result=_book).dict(exclude_none=True)

@router.get('/{id}')
async def get_by_id(id: int, db:Session=Depends(get_db)):
  _book = crud.get_book_by_id(db, book_id=id)
  return Response(code=200, status='Ok', message='Success get data', result=_book).dict(exclude_none=True)

@router.post("/create")
async def create_book_service(request: RequestBookCreate, db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully").dict(exclude_none=True)


@router.patch("/update")
async def update_book(request: RequestBookUpdate, db: Session = Depends(get_db)):
    _book = crud.update_book(db, book_id=request.parameter.id,
                             title=request.parameter.title, description=request.parameter.description)
    return Response(status="Ok", code="200", message="Success update data", result=_book)


@router.delete("/delete")
async def delete_book(request: RequestBookDelete,  db: Session = Depends(get_db)):
    crud.remove_book(db, book_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
