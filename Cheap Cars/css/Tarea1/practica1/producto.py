class producto:
    def __init__(self,nombre,valor,desc,cant) :
        self.nombre=nombre
        self.valor=valor
        self.desc=desc
        self.cant=cant

c= int(input("¿cuantos productos ingresara? "))        

productos=[]

for i in range(c):
    print("Producto numero: ",i+1)
    n=input("Nombre del producto: ")
    vr=int(input("valor del producto: "))
    desc=input("descripcion del producto: ")
    cant=int(input("cantidad del producto: "))
    p=producto(n,vr,desc,cant)
    productos.append(p)

    print("=====listado de productos====")
    for j in range (len(productos)):
        print("Nombre:",productos[j].nombre)
        print("Descripcion:",productos[j].desc)
        print("Valor:",productos[j].valor)
        print("Cantidad:",productos[j].cant)
        print("================================")