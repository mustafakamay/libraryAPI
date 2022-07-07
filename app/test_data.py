from ntpath import join
import random
import string
from random import randrange
from bson.objectid import ObjectId
import redis
import pymongo
from fastapi import APIRouter, Body


router = APIRouter()

@router.post("/add")
def test_data_added():
    client = pymongo.MongoClient("localhost",27017)
    database = client.library

    book_collection = database.get_collection("books")
    user_collection = database.get_collection("users")

    letters = string.ascii_uppercase
    random.seed(42)

    list_of_books = []
    list_of_user = []
    for i in range(50):
        user = {
            "email":"".join(random.choice(letters) for i in range(15))+ "@" + "".join(random.choice(letters) for i in range(5)),
            "fullname": ''.join(random.choice(letters) for i in range(7)) + " " + ''.join(random.choice(letters) for i in range(8)),
        }
        list_of_user.append(user)
        print(user)
    user_collection.insert_many(list_of_user)
    for x in range(100000):
        book = {
                "name": ''.join(random.choice(letters) for i in range(50)),
                "author": ''.join(random.choice(letters) for i in range(7)) + " " + ''.join(random.choice(letters) for i in range(8)),
                }
        print(book)
        list_of_books.append(book)

    book_collection.insert_many(list_of_books)
    return True