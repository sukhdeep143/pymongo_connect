import pymongo


if __name__ == "__main__" :
    print("MongoDB is Conneted successfully !!!")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    
    db = client["Test_database"]
    collection = db["This is a database collection !!!"]
    
    # one = collection.find_one({"name" : "aman"})
    # print(one)

    FindAll = collection.find({"name" : "aman"}, {"name" : 1, "_id" : 0})
    
    for item in FindAll:
     print(item)
    
    
    
    
    