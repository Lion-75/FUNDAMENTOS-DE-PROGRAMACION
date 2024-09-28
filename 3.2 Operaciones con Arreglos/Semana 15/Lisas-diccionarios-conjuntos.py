#Creamos un diccionario informacion_personal

#informacion_personal
print("_______________________________________________________________________________________")
persona={
    "nombre":"Mathew",
    "apellido":"Macas",
    "edad": 13,
    "sexo": "M"
}

#Obtener valores
print("nombre: ", persona["nombre"])
print("apellido: ", persona["apellido"])
print("edad: ", persona["edad"])
print("sexo: ", persona["sexo"])

#modificacion de la clave
print("_______________________________________________________________________________________")
persona["edad"] = 32

#agregar nueva clave
print("_______________________________________________________________________________________")
persona["Profesion"] = "Ingeniero en Mecatrónica"
print("todo: ", persona)

#Eliminar un par clave
print("_______________________________________________________________________________________")
del persona["apellido"]
print("todo: ", persona)

#imprime clave
print("_______________________________________________________________________________________")
clave = persona.keys()
print("Imprime las claves", clave)

#Imprimir valor
print("_______________________________________________________________________________________")
valores = persona.values()
print("Imprime valores: ", valores)

#recorrer con un for
print("_______________________________________________________________________________________")
for clave, valor in persona.items():
    print(clave," : ", valor)

# Agregar conjuntos (Ciudades)
print("_______________________________________________________________________________________")
print("Conjuntos: ")

ciudad ={"cuenca", "quito", "guayaquil" }
print(ciudad)

# agregar
ciudad.add("ambato")
print(ciudad)

ciudad.add("cuenca")
print(ciudad)

#eliminar
print("_______________________________________________________________________________________")
ciudad.remove("quito")
print(ciudad)