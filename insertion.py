import pymongo


if __name__ == "__main__" :
    print("MongoDB is Conneted successfully !!!")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    
    db = client["Test_database"]
    collection = db["This is a database collection !!!"]
    
    dictionary = [
        {"name" : "sukhdeep", "age" : 22, "location" : "punjab"},
        {"name" : "harman", "age" : 22, "location" : "punjab"},
        {"name" : "aman", "age" : 23, "location" : "punjab"},
        {"name" : "god", "age" : 999999, "location" : "punjab"},
        {"name" : "sukhdeep", "age" : 22, "location" : "punjab"},
        {"name" : "harman", "age" : 22, "location" : "punjab"},
        {"name" : "aman", "age" : 23, "location" : "punjab"},
        {"name" : "god", "age" : 999999, "location" : "punjab"}
    ]
    
    

    collection.insert_many(dictionary)
    
    # dictionary = {
    #     'Name' : "Sukhdeep",
    #     'Marks' : 77
    # }
    
    # collection.insert_one(dictionary)
    

