import os
import requests
from bson import ObjectId
from celery import Celery

from pymongo import MongoClient


broker = os.getenv("CELERY_BROKER_URL")
backend = os.getenv("CELERY_RESULT_BACKEND")
celery = Celery("fast-api-tasks", broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/0")


mongo_uri = os.getenv("MONGODB_URL")




@celery.task
def borrow_book_task(user_id, book_id):
    for i in range(100000):
        data = requests.post(f"localhost:///borrow/{user_id}/{book_id}")
        refund_data = requests.post(f"localhost://refund/{book_id}")
    return refund_data