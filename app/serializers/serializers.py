def bookSerializer(book) -> dict:
    return {
        "id": str(book["_id"]),
        "name": book["name"],
        "author": book["author"]
    }

def interactionsSerializer(book) -> dict:
    return {
        "book_id": book["book"]["id"],
        "book_name": book["book"]["name"],
        "user_id": book["user"]["id"],
        "user_email": book["user"]["email"],
        "user_lastname": book["user"]["fullname"]
    }
def userSerializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "fullname": user["fullname"]
    }