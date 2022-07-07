from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.database.interactions import (
    checkBook,
    refundBook,
    getBorrowedBooks,
    borrowBook
)
from app.models.book import (
    ResponseModel,
    ErrorResponseModel,
)
router = APIRouter()

@router.post('/borrow/{user_id}/{book_id}', response_description="Borrow a book.")
async def borrow_book(user_id, book_id):
    result = borrowBook(user_id, book_id)
    if result == False:
        return JSONResponse(status_code=400,content="This book is borrowed")
    return ResponseModel("Borrowed", 200)

@router.delete('/return/{book_id}', response_description="Return book to library.")
async def return_book(book_id):
    if checkBook(book_id):
        deleted_book = refundBook(book_id)
        if deleted_book:
            return ResponseModel("The book has been refunded.", 204)
        return ErrorResponseModel("Something went wrong", 404)
    else:
        return ErrorResponseModel("This book is not avaible", 404)

@router.get('/borrowed', response_description="Get borrowed books.")
async def borrowed_book():
    books = getBorrowedBooks()
    if books:
        return ResponseModel(books, "Books data ")
    return ResponseModel(books, "Empty list returned.")