#Sintáxis de una tupla 
tupla = (1, 56.5, 85, "Python")

print(type(tupla))

#Acceso por índice
print("Elemento en la posición 2: ", tupla[2])

numeros = (2, 5, 8, 7, 6, 1, 3, 1)
print("Cuántas veces aparece el número 1: ", numeros.count(1))
print("índice del número 8: ", numeros.index(8))

tupla3 = tupla + numeros
print("Concatenar tuplas: ", tupla3)

###Una tupla no es mutable

tupla[3] = "C++"
print(tupla)