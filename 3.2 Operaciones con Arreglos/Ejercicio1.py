# Crear una matriz 3x3
matriz= [[1, 20, 9],
         [6, 8, 19],
         [3, 45, 2]
         ]
print(matriz)

#Función: Buscar un valor especifico

def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
         for j in range(len(matriz)):
            if matriz[i][j] == valor_buscado:
                return i, j

valor_buscado = 19
#print(buscar_valor(matriz, valor_buscado))

if valor_buscado == valor_buscado:
    print("valor encontrado en la posicion", buscar_valor(matriz, valor_buscado))
else:
    print("valor incorrecto")