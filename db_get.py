import pymongo
myclient = pymongo.MongoClient("mongodb://admin:research21@ec768aa3-bb97-421c-98bd-4822fa7dbea1-0.b8267831955f40ef8fb5530d280e5a10.databases.appdomain.cloud:32481,ec768aa3-bb97-421c-98bd-4822fa7dbea1-1.b8267831955f40ef8fb5530d280e5a10.databases.appdomain.cloud:32481,ec768aa3-bb97-421c-98bd-4822fa7dbea1-2.b8267831955f40ef8fb5530d280e5a10.databases.appdomain.cloud:32481/ibmclouddb?authSource=admin&replicaSet=replset", ssl=True, ssl_ca_certs="cert/5fa7d040-a1ec-11e9-a59f-6a9a0379346c")

db = myclient["STOCK"]
collection = db["EikonDescription"]

f = open("./data/data.txt", "a")

item_details = collection.find()
for item in item_details:
    #print(item['ticker_name'],item['text'])
    f.write(item['ticker'])
    f.write(", ")
    f.write(str(item['text']))
    f.write("<|endoftext|>\n")

f.close()

#stock - eikon_description -> ticker_name, text
