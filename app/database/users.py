import pymongo
from bson.objectid import ObjectId
from ..serializers.serializers import userSerializer
client = pymongo.MongoClient("localhost", 27017)
database = client.library
user_collection = database.get_collection("users")



def retrieve_users():
    users = []
    try:
        for user in user_collection.find({}):
            print(user)
            users.append(userSerializer(user))
    except:
        pass
    return users

def userDetail(id: str) -> dict:
    user = user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return userSerializer(user)

def userAdd(user_data: dict) -> dict:
    user = user_collection.insert_one(user_data)
    new_user = user_collection.find_one({"_id": user.inserted_id})
    return userSerializer(new_user)

def userUpdate(id: str, data: dict):
    if len(data) < 1:
        return False
    user = user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = user_collection.update_one({"_id":ObjectId(id)}, {"$set":data})
        if updated_user:
            return True
        return False

def userDelete(id: str):
    user = user_collection.find_one({"_id": ObjectId(id)})
    if user:
        user_collection.delete_one({"_id": ObjectId(id)})
        return True