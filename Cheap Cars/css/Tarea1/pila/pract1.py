lista=list()

class Alumnos:
    def _init_(self):
         self.nombre=(" ")
         self.edad=()
         self.matricula=()
         self.carrera(" ")

    

def menu ():
    seleccion=0
    while seleccion!=4:    
        #Menu
        print ("Bienvenidos al menu")
        print ("1. Registrar alumno")
        print ("2. Listar alumnos")
        print ("3. Buscar alumnos")
        print ("4. salir")
        seleccion= int(input("Elija una opcion: "))

    if seleccion==1:
     registrar()
    if seleccion==2:
     mostrar()
    if seleccion==3:
     buscar()
    if seleccion==4:
     salir()         

def registrar():
   print("Registra alumnos")       
   alumno=Alumnos()
   alumno.nombre=input("Introduce el nombre: ")
   alumno.edad=input("Introduce la edad: ")
   alumno.matricula=input("Introduce la matricula: ")
   alumno.carrera=input("Introduce la carrera que cursas: ")
   lista.append(alumno)

def mostrar():
    print("mostrar alumnos")
    for alumno in lista:
       print("El nombre del alumno es:",alumno.nombre,"de matricula",alumno.matricula,"con edad de",alumno.edad)

def buscar():
   print("Buscar alumnos")
   matricula=input("Ingrese matricula")
for alumno in lista:
   print(alumno.nombre,"-",alumno.matricula,"-",alumno.edad,"-",alumno.carrera)

def salir():
   print("!Gracias!")     
   

menu()