datos = {
    "muestra_id": 101,
    "valor_medido" : 2.5,
    "unidad" : "mg/L",
    "control" : False,
    "etapa_proceso" : "filtrado"
}

print("Datos originales: ", datos)

#Eliminar datos de un diccionario

valor_eliminado = datos.pop("valor_medido", None) #None si no existe la clave
print("Después de pop('valor_medido'): ", datos, "| Valor eliminado: ", valor_eliminado)

#Tambíen se puede utilizar del
del datos["unidad"]
print("Después de 'del' datos['unidad']: ", datos)

datos = {
    "muestra_id": 101,
    "valor_medido" : 2.5,
    "unidad" : "mg/L",
    "control" : False,
    "etapa_proceso" : "filtrado"
}

print("\nDiccionario reiniciado", datos)

#Limpiar un diccionario completo
#datos.clear()
#print("Después de clear(): ", datos)

##Método get evita errores al acceder a claves ausentes
valor_algo = datos.get("hola", "Clave no encontrada, intenta con otra")
print("Valor de 'hola' usando get(): ", valor_algo)

#setdefault: garantiza que una clave exista con su valor por defecto
#En caso de que el método no encuentre la clave, la crea y le asigna
#el valor con el segundo parámetro ("desconocida")
resultado_setdefault = datos.setdefault("fuente de datos", "desconocida")
print('setdefault("fuente de datos", "desconocida") devolvió: ', resultado_setdefault)
print("Diccionario tras setdefault: ", datos)

datos_actualizados = {
    "limite_superior" : 5.0,
    "limite_inferior" : 0.3
}

#Actualizar un diccionario (combinar datos)
datos.update(datos_actualizados) #Actualiza/ añade pares clave:valor
print("Después de update(): ", datos)

#datos_nuevos = datos.update(datos_actualizados) #Actualiza/ añade pares clave:valor
#print("Después de update(): ", datos)

#Copiar un diccionario
CopyDatos = datos_actualizados.copy()
print("\nCopia del diccionario: ", CopyDatos)

maximo = max(datos_actualizados.values())
print("Valor máximo del diccionario: ", maximo)

#Inspección de los datos de un diccionario
print("\nLlaves del diccionario: ", datos.keys())
print("\nLlaves del diccionario: ", list(datos.keys()))

for algo in (datos.keys()):
    print(algo)
    print(f"El valor de {algo} es: {datos[algo]}")

print("\nValores del diccionario: ", list(datos.values()))
print("\nItems (clave, valor): ", list(datos.items()))

peliculas = {
    "Inception" : 12,
    "Avatar" : 9,
    "Interestellar" : 15,
    "Titanic" : 7, 
    "Avengers" : 20
}

#Encontrar la película más votada
mas_popular = max(peliculas, key=peliculas.get)

print("La película más popular es: ", mas_popular, "con", peliculas[mas_popular], "votos" )