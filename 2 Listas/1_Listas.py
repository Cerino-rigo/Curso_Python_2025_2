# Listas heterogéneas
lista = ["Python", 100, "Nombre", 3.14, 6.28]
print(lista)
print("Tipo de estructura: ", type(lista))

print("Elemento en la posición 4: ", lista[4])
print("Longitud de la lista: ", len(lista))

ventas_diarias = [45, 67, 89, 34, 78, 56, 23]

#Una lista es mutable
ventas_diarias[0] = 54 #Corrección de datos
print("Después de la corección: ", ventas_diarias)

#Devanado de listas
print("Días hábiles: ", ventas_diarias[0:5])
print("Ventas de fin de semana: ", ventas_diarias[-2:])

#Crear una lista de 10 números y muestra solo los que estén en posiciones impares

numeros = [12, 56, 33, 25, 14, 17, 19, 15, 78, 100]
print(numeros[1::2])