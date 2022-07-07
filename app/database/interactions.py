import pymongo
from bson.objectid import ObjectId
from ..serializers.serializers import interactionsSerializer
from .books import bookDetail
from .users import userDetail
from fastapi.responses import JSONResponse

client = pymongo.MongoClient("localhost", 27017)
database = client.library
collection = database.get_collection("reservedBooks")

def borrowBook(user_data: int, book_data: int) ->dict:
    userData = userDetail(user_data)
    bookData = bookDetail(book_data)
    if collection.find_one({"book": bookData}):
        return False
    print("out")
    data = {
        "user": userData,
        "book": bookData
    }
    reserve_book_data = collection.insert_one(data)
    new_reserve_book_data = collection.find_one({"_id": reserve_book_data.inserted_id})
    return new_reserve_book_data

def checkBook(book_id: str):
    for books in collection.find():
        if books["book"]["id"] == book_id:
            return True
    return False

def refundBook(book_id):
    id = ""
    for books in collection.find():
        if books["book"]["id"] == book_id:
           id = books["_id"]
    borrowed_book = collection.find_one({"_id": ObjectId(id)})
    if borrowed_book:
        collection.delete_one({"_id": ObjectId(id)})
        return True
def getBorrowedBooks():
    books = []
    for book in collection.find():
        books.append(interactionsSerializer(book))
    return books