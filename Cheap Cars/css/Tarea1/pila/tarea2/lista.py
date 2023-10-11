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



