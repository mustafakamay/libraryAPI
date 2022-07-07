import os
import pymongo
from bson.objectid import ObjectId
import redis
import ast
from ..serializers.serializers import bookSerializer

client = pymongo.MongoClient("localhost",27017)
database = client.library

book_collection = database.get_collection("books")
r = redis.Redis(os.getenv("REDIS"))




def addBook(book_data: dict) -> dict:
    book =  book_collection.insert_one(book_data)
    new_book =  book_collection.find_one({"_id": book.inserted_id})
    return bookSerializer(new_book)

def bookDetail(id: str) -> dict:
    book =  book_collection.find_one({"_id": ObjectId(id)})
    if book:
        return bookSerializer(book)

def bookUpdate(id: str, data: dict):
    if len(data) < 1:
        return False
    book =  book_collection.find_one({"_id": ObjectId(id)})
    if book:
        updated_book =  book_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        if updated_book:
            return True
        return False

def bookDelete(id: str):
    book = book_collection.find_one({"_id":ObjectId(id)})
    if book:
        book_collection.delete_one({"_id":ObjectId(id)})
        return True