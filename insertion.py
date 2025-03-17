import pymongo


if __name__ == "__main__" :
    print("MongoDB is Conneted successfully !!!")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    
    db = client["Test_database"]
    collection = db["This is a database collection !!!"]
    
   

    
    dictionary = [
        {"name": "Mani", "age": 28, "city": "Mumbai"},
    {"name": "Sukhmani", "age": 24, "city": "Bangalore"}
    ]
    
    

    collection.insert_many(dictionary)
    
    # dictionary = {
    #     'Name' : "Sukhdeep",
    #     'Marks' : 77
    # }
    
    # collection.insert_one(dictionary)
    

