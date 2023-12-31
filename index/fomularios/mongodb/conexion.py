import pymongo

MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_TIEMPO_FUERA = 1000

MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

MONGO_BASEDATOS = "carros"
MONGO_COLECCION = "descripcion"


try:
 cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
 baseDatos=cliente[MONGO_BASEDATOS]
 coleccion=baseDatos[MONGO_COLECCION]
 for documento in coleccion.find():
  print(documento["Marca"]+" "+documento["Modelo"]+" "+str(documento["Costo"]))
   #cliente.server_info()
 #print("conexion a mongo exitosa")
 cliente.close()
except pymongo.errors.serverSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido"+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb"+errorConexion)


    