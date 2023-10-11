from  pymongo import MongoClient

client=MongoClient('localhost')

db=client['carros']
col=db ['descripcion']

query_del={

     "ID":99    

}
col_del=col.delete_one(query_del)


