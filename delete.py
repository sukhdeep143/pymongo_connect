import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print("Your connected to the MongoDB !!!")
    
    db = client["Test_database"]
    collection = db["This is a database collection !!!"]
    
    record_delete = {"name" : "aman"}
    
    # data_To_delete = collection.delete_one(record_delete)
    data_To_delete = collection.delete_many(record_delete)
    print(data_To_delete.deleted_count, "Data is deleted!!")
    