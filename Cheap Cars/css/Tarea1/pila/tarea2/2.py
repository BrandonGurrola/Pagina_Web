def main():
  numero = int(input("Dime cuántas palabras tiene la primera lista: "))

  if numero < 1:
      print("¡Incorrecto!")
  else:
      primera = []
      for i in range(numero):
          palabra = input(f"Digame la palabra {i + 1}: ")
          primera += [palabra]
      print(f"La primera lista es: {primera}")

      for i in range(len(primera) - 1, -1, -1):
          if primera[i] in primera[:i]:
              del primera[i]

      numero2 = int(input("Dime cuántas palabras tiene la segunda lista: "))

      if numero2 < 1:
          print("¡Incorrecto!")
      else:
          segunda = []
          for i in range(numero2):
              palabra = input(f"Digame la palabra {i + 1}: ")
              segunda += [palabra]
          print(f"La segunda lista es: {segunda}")

          for i in range(len(segunda) - 1, -1, -1):
              if segunda[i] in segunda[:i]:
                  del segunda[i]

          comunes = []
          for i in primera:
              if i in segunda:
                  comunes += [i]
          print(f"Palabras que aparecen en las dos listas: {comunes}")

          soloPrimera = []
          for i in primera:
              if i not in segunda:
                  soloPrimera += [i]
          print(f"Palabras que solo aparecen en la primera lista: {soloPrimera}")

          soloSegunda = []
          for i in segunda:
              if i not in primera:
                  soloSegunda += [i]
          print(f"Palabras que solo aparecen en la segunda lista: {soloSegunda}")

          todas = comunes + soloPrimera + soloSegunda
          print(f"Todas las palabras: {todas}")


if __name__ == "__main__":
  main()