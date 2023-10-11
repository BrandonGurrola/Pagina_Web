'import numpy as np'
'mi_matriz = np.array([["B", 0,"R", 6, 9, "A"], [9, 0, 5, "M", 8, 1], [0, 99, "G", 27, 17,0]])'
'print("La matriz es: ")'
'print(mi_matriz)'


filas=int(input("Introduce numero de filas: "))
columnas=int(input("Introduce numero de columnas: "))

matriz= []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor=float(input("fila {}, columna {}: ".format(i+1, j+1)))
        matriz[i].append(valor)


print()
for fila in matriz:
    print("[",end=" ")
    for elemento in fila:
        print("{:4.2f}".format(elemento),end=" ")
    print("]") 
print()       