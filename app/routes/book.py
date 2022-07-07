from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

# from app.database.borrowBooks import (
#     checkBook,
#     delete_borrow_book,
#     get_borrowed_books
# )
from app.database.books import (
    addBook,
    bookDelete,
    bookUpdate,
    bookDetail
)

from app.models.book import (
    ResponseModel,
    ErrorResponseModel,
    BookSchema,
)
# from app.server.tasks import borrow_book_task

router = APIRouter()

@router.post("/add")
async def add_book_data(book: BookSchema = Body(...)):
    book = jsonable_encoder(book)
    new_book = addBook(book)
    return ResponseModel(new_book, "Book added.")

# @router.get("/", response_description="Books retrieved")
# def get_books():
#     books = get_all_books()
#     if books:
#         return ResponseModel(books,"All books list")
#     return ResponseModel(books, "Empty list returned.")

@router.get("/detail/{id}")
async def get_book_data(id):
    book = bookDetail(id)
    if book:
        return ResponseModel(book, "Book detail.")
    return ErrorResponseModel("Book does not exist", 404)

@router.put("/update/{id}")
async def update_book_data(id, req: BookSchema = Body(...)):
    req = {k : v  for k, v in req.dict().items() if v is not None}
    updated_book = bookUpdate(id, req)
    if updated_book:
        return ResponseModel(updated_book, "Updated successfully,")
    return ErrorResponseModel("Something went wrong", 404)

@router.delete("/delete/{id}")
async def delete_book_data(id:str):
    deleted_book = bookDelete(id)
    if deleted_book:
        return ResponseModel(deleted_book, "Book deleted successfully.")
    return ErrorResponseModel("Something went wrong", 404)

# @router.post('/borrow/{user_id}/{book_id}', response_description="Borrow a book.")
# async def borrow_book(user_id, book_id):
#     borrow_book_task.delay(user_id, book_id)
#     return ResponseModel("Task started", "Borrowed.")

# @router.delete('/return/{book_id}', response_description="Return book to library.")
# async def return_book(book_id):
#     if checkBook(book_id):
#         deleted_book = delete_borrow_book(book_id)
#         if deleted_book:
#             return ResponseModel("The book has been returned.", "The book has been returned")
#         return ErrorResponseModel("An error occured.", 404, "The book could not be returned.")
#     else:
#         return ErrorResponseModel("This book is not on loan", 404, "This book is not on loan.")

# @router.get('/borrowed', response_description="Get borrowed books.")
# async def borrowed_book():
#     books = get_borrowed_books()
#     if books:
#         return ResponseModel(books, "Books data retrieved successfully.")
#     return ResponseModel(books, "Empty list returned.")