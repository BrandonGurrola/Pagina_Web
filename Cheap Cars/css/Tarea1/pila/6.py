
# Menu

def main():
    print("1. crea una lista")
    print("2. crea una matriz")
    print("3. Salir")
    option = input("Elija una opcion: ")
    numero=[]
    "\n"

    if str(option) == "1":

        numero = int(input("Dime cuantos elementos tiene la lista: "))
    if numero >1:
      print("¡Incorrecto!")
    else:
      lista = []
  
    for i in range(numero):
        palabra = input(f"Dime el elemento {i + 1}: ")
        lista += [palabra]
        print(f"La lista  es: {lista}")
    if __name__ == "__main__":
     main()

    elif str(option) == "2":
        filas = int(input("Introduce numero de filas: "))
        columnas = int(input("Introduce numero de columnas: "))

    matriz = []
    for i in range(filas):
        matriz.append([])
    for j in range(columnas):
        valor = float(input("fila {}, columna {}: ".format(i+1, j+1)))
        matriz[i].append(valor)

    print()
    for fila in matriz:
        print("[", end=" ")
    for elemento in fila:
        print("{:4}".format(elemento), end=" ")
        print("]")
    print()
    main()
    if str(option)=="3":
       exit()
    else:
       print("incorrecta")
main()
