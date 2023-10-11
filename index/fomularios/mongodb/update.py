from  pymongo import MongoClient

client=MongoClient('localhost')

db=client['carros']
col=db ['descripcion']

query={
    "ID":89
}

query_val={
    "$set":{"ID":99}
}
col_up=col.update_one(query,query_val)

