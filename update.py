import pymongo


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print("MongoDB connected!!")
    
    db = client["Test_database"]
    collection = db["This is a database collection !!!"]
    
    old_value = {"name" : "sukhdeep"}
    update_value = {"$set":
        {"location" : "mumbai"}
        }
    
    # update_data = collection.update_one(old_value, update_value)
    update_value = collection.update_many(old_value, update_value)

    print("Data is update!!")
    