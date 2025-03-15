import pymongo


if __name__ == "__main__" :
    print("MongoDB is Conneted successfully !!!")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)