import pymongo

client = pymongo.MongoClient("mongodb+srv://JackSmith:Bassline@cluster0.ilfjv4i.mongodb.net/?retryWrites=true&w=majority")
db = client.test

mydb = client["bbdd"]
mycol = mydb["clientes"]

mydict = {"Nombre": "Martin Elias", "Direccion": "C/ Mayor 3"}

x = mycol.insert_one(mydict)
print(x.inserted_id)

for x in mycol.find({"Direccion":1}):
    print(x)
    