#!/home/paco/py3/bin/python
from pymongo import MongoClient

#1. Connect to the following database:
info_db = {
  "username": "mongo_pc_lvl3",
  "password": "ffb7d1fec8b161bbf6c6dc398b731d0afa6aea0a",
  "database": "task_mongo_pc_lvl3",
  "mongoServers": [{"host": "bdb-dbaas-alln-2.cisco.com","port": 27001}]
}

#2. In the PC_USERS collection, write a new object, as follows:
collection = "PC_USERS"

my_info = {'cec_id':"frquiroz",
            'preferred_name':"paco" }

yo = {'cec_id':"frquiroz"}

def connect_to_mongo_db(var_info_db):
    db = var_info_db["database"]
    list_clients = [MongoClient(server["host"],server["port"],username=var_info_db["username"],password=var_info_db["password"],authSource=var_info_db["database"]) for server in var_info_db["mongoServers"]]
    list_db = [client[db] for client in list_clients ]
    return list_db

def get_collections(collection,var_db_list):
    list_collections = [ db[collection] for db in var_db_list]
    return list_collections

def my_insert(var_list_collections,data):
    list_results = [ collection.insert_one(data) for collection in var_list_collections]
    return list_results

def my_delete(var_list_collections,data):
    list_results = [ collection.delete_one(data) for collection in var_list_collections]
    return list_results
        
def lista(cl):
    n = 0 
    for c in cl:
        print (n)
        for i in c.find():
            print(i)
        n += 1

dl = connect_to_mongo_db(info_db)
cl = get_collections(collection,dl)
lista(cl)

r= my_insert(cl,my_info)
lista(cl)

r= my_delete(cl,yo)
lista(cl)

"""
from ch2_w2_frquiroz import *
client = MongoClient("bdb-dbaas-alln-2.cisco.com",27001,username="mongo_pc_lvl3",password="ffb7d1fec8b161bbf6c6dc398b731d0afa6aea0a",authSource="task_mongo_pc_lvl3")
db = client["task_mongo_pc_lvl3"]
col = db[collection]

d = connect_to_mongo_db(info_db)
col = dl[0][collection]
col.find_one()
"""
