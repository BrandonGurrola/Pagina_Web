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