import pymongo

client = pymongo.MongoClient("mongodb+srv://Dingo:1234@cluster0.8evqx.mongodb.net/")
    
mydb = client["POSTS"]
    
coll = mydb["ashua"]


query={
    "id":6
}
x=coll.find_one(query)

print(x)