stack = []

#Menu
def main():
        print("1. Apilar un elemento")
        print("2. Desapilar un elemento")
        print("3. Mostrar pila")
        print("4. Salir")
        option = input("Elija una opcion: ")
        "\n"

        #Apila el numero en la pila:
        if str(option)=="1":
                elemento = input(" Introduce un numero: ")
                stack.append(elemento)
                print("Insertado correctamente")
                main()
                "\n"

        #Desapila el ultimo numero ingresado a la pila:
        elif str(option)=="2":
                if len(stack) == 0:
                   print(" No hay elementos para desapilar ")
                   main()
                else:
                   print("El numero: ",stack.pop()," fue desapilado")
                   main()

        #imprime la pantalla:     
        elif str(option)=="3":
                for i in reversed(range(len(stack))):
                   print("Pila: ",stack[i])
                main()

        #salir del codigo:
        elif str(option)=="4":
                exit()
        else:
                print("\nOpcion incorrecta.\n")
                main()

main()