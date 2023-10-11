'''
Programa1
'''

'nombre=input("Introduce tu nombre: ")'
'print("¡Hola "  +   nombre  + "!")'

'''
programa2
'''
'''print(((3 + 2) / (2 * 5)) ** 2)'''

'''
programa3
'''
'horas = float(input("Introduce tus horas trabajadas: "))'
'costo = float(input("Introduce lo que cobras por hora: "))'
'pago = horas * costo'
'print("Tu pago es de :", pago)'

'''
programa4
'''
'peso = input("¿Cuál es tu peso?")'
'estatura = input("¿Cuál es tu estatura?")'
'imc = round(float(peso)/float(estatura)**2,2)'
'print("Tu masa corporal es de: " + str(imc))'

'''
programa5
'''
'cantidad = float(input("¿Cantidad a invertir? "))'
'interes = float(input("¿Interés anual? "))'
'años = int(input("¿Años?"))'
'print("Capital: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))'


'''
programa6
'''
'payaso = 112'
'muñeca = 75'
'payasos = int(input("Introduce el número de payasos a enviar: "))'
'muñecas = int(input("Introduce el número de muñecas a enviar: "))'
'total = payaso * payasos + muñeca * muñecas'
'print("El peso total es: " + str(total))' 

'''
programa7
'''
'inversion = float(input("Introducir la inversion: "))'
'interes = 0.04'
'ahorro1 = inversion * (1 + interes)'
'print("Ahorro del primer año: " + str(round(ahorro1, 2)))'
'ahorro2 = ahorro1 * (1 + interes)'
'print("Ahorro del segundo año: " + str(round(ahorro2, 2)))'
'ahorro3 = ahorro2 * (1 + interes)'
'print("Ahorro del tercer año: " + str(round(ahorro3, 2)))'

'''
programa8
'''
numero = int(input("Introduce un número entero: "))
suma = numero * (numero + 1) / 2
print("La suma de los números enteros desde 1 hasta " + str(numero) + " es " + str(suma))