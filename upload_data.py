from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri = "mongodb+srv://naman:12345@cluster0.ocqju.mongodb.net/?retryWrites=true&w=majority"

# create new client and connect to server
client = MongoClient(uri)

# create database name and collection name 
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"

df = pd.read_csv("D:\PW Skills\Projects\ML Sensor Fault Detection\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis = 1)

json_record = list(json.loads(df.T.to_json()).values()) # df converted into json list for mongodb
type(json_record)

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record) # inserted into mongodb
