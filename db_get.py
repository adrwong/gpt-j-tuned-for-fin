import pymongo
import os
import errno

myclient = pymongo.MongoClient("mongodb://admin:research21@ec768aa3-bb97-421c-98bd-4822fa7dbea1-0.b8267831955f40ef8fb5530d280e5a10.databases.appdomain.cloud:32481,ec768aa3-bb97-421c-98bd-4822fa7dbea1-1.b8267831955f40ef8fb5530d280e5a10.databases.appdomain.cloud:32481,ec768aa3-bb97-421c-98bd-4822fa7dbea1-2.b8267831955f40ef8fb5530d280e5a10.databases.appdomain.cloud:32481/ibmclouddb?authSource=admin&replicaSet=replset", ssl=True, ssl_ca_certs="cert/5fa7d040-a1ec-11e9-a59f-6a9a0379346c")

db = myclient["NLP"]
collection_ECT = db["CleanECT"]
collection_News = db["CleanNewsFilter"]
item_details_ECT = collection_ECT.find()
print("retrieving clean ect...")
count = 0
for item in item_details_ECT:
    #print(item['ticker_name'],item['text'])
    filename = "../data_for_gptj/ect/"+ str(item['_id']) + ".txt"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    
    
    fect = open(filename, "a", encoding='utf-8')
    fect.write(str(item['text']))
    fect.write("<|endoftext|>\n")
    fect.close()
    count += 1
    if count % 1000 == 0:
        print(str(count + 1) + " documents have been processed")
print("retrieving clean ect completed")


item_details_News = collection_News.find()
print("retrieving news...")
for item in item_details_News:
    #print(item['ticker_name'],item['text'])
    filename = "../data_for_gptj/news/"+ str(item['_id']) + ".txt"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    fnews = open(filename, "a", encoding='utf-8')
    fnews.write(str(item['title']))
    fnews.write(str(item['description']))
    fnews.write(str(item['content']))
    fnews.write("<|endoftext|>\n")
    fnews.close()
    count += 1
    if count % 1000 == 0:
        print(str(count + 1) + " documents have been processed")

print("retrieving news completed")

