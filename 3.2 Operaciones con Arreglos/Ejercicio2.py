# Crear una matriz 3x3
matriz= [[14, 20, 34],
         [23, 35, 11],
         [38, 41, 82]

         ]
print(matriz)

#metodo de ordenamiento de la fila buble_sort
def buble_sort(fila):
    #algoritmo buble sort
    n = len(fila)
    for i in range (n):
        for j in range(n-1, i, -1 ):
            if fila[j] > fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                print(fila)

print("Matriz original")
print(matriz)
buble_sort(matriz[1])
print(matriz)