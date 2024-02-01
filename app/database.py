from pymongo import MongoClient
from pymongo.collection import Collection


# Replace with your connection string (ensure you include your username and password)
MONGO_DETAILS = "mongodb+srv://rishikesh20032000rishikesh:rishikesh1234@cluster0.nqkz8sb.mongodb.net/"
client = MongoClient(MONGO_DETAILS)

# Replace 'your_db_name' with your actual database name
db = client.blog_api

# Example to access a collection
# Replace 'your_collection_name' with your actual collection name
user_collection = db.get_collection("users_collection")
blog_collection = db.get_collection("blogs_collection")
item_collection = db.get_collection("item_collection")

