from  pymongo import MongoClient

client=MongoClient('localhost')

db=client['carros']
col=db ['descripcion']

col.insert_one({
    'ID':89,
    'Vendedor': 'Fanny M',
    'Comprador': 'Dayanna R',
    'Marca': 'Nissan',
    'Modelo': 'Versa',
    'Color': 'Green',
    'Año': 2019,
    'Costo': 4500,
})

   

