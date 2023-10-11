class producto:
    def __init__(self,nombre,valor,desc,cant) :
        self.nombre=nombre
        self.valor=valor
        self.desc=desc
        self.cant=cant
def menu ():
    seleccion=0
    while seleccion!=4:    
        #Menu
        print ("Bienvenidos al menu")
        print ("1. productos")
        print ("2. casa de cambio")
        print ("3. empleados")
        print ("4. lista")
        seleccion= int(input("Elija una opcion: "))

    if seleccion==1:
     productos()
    if seleccion==2:
     hl()
    if seleccion==3:
     objeto_persona ()
    if seleccion==4:
     main()


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


print("1: de dolares a euros")
print("2: de euros a dolares")
print("3: de pesos mexicanos a dolares")
print ("")
hl=int(input("Elije una opcion: "))
print ("")


if hl==1:
    dol3=int(input("introduce cantidad de dolares: "))
    euros=dol3*18.57
    print("")
    print("euros=", euros)
if hl==2:
    euros1=int(input("introduce cantidad de euros: "))
    dol4=euros1*17.27
    print("")
    print("dolares=", dol4)
if hl==3:
    pesm=int(input("Introduce cantidad de pesos : "))
    dol5=pesm*17.27
    print("")
    print("dolares=", dol5)

    print("=======================================")

def objeto_persona():
    Nombre = str(input("Introuce el nombre: "))
    Apellidos = str(input("Introduce tus apellidos: "))
    Edad = int(input("Introduce edad: "))
    Salario = float(input("Introduce salario: "))
    persona = [Nombre, Apellidos, Edad, Salario]
    print("==================================")
    return persona
 
def imprimir_persona(lista):
    for i in lista:
        print("Elementos en lista: {0}".format(i))
 
 
lista_de_personas = (objeto_persona())
#Crear mas objetos personas
lista_de_personas.extend(objeto_persona())
 
print(lista_de_personas)


def main():
  numero = int(input("Dime cuantos elementos tiene la lista: "))

  if numero < 1:
      print("¡Incorrecto!")
  else:
      lista = []
      for i in range(numero):
          palabra = input(f"Dime el elemento {i + 1}: ")
          lista += [palabra]
      print(f"La lista  es: {lista}")


if __name__ == "__main__":
  main()

menu()