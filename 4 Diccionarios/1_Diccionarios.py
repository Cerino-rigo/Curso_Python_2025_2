# Sintáxis de un diccionario {clave:valor}
diccionario = {'Nombre' : "Rigo", 'Contraseña' : 123456, 'Estatura' : 1.70}

print("Mi primer diccionario: ", diccionario)
print("Tipo de estructura: ", type(diccionario))
print("La longitud del diccionario es: ", len(diccionario))

##No insertar 2 claves iguales, ya que las reemplaza
diccionario2 = {'Nombre' : "Rigo", 'Contraseña' : 123456, 'Nombre' : "Cerino"}
print(diccionario2)

##Acceder a las claves del diccionario
print(diccionario.keys())

##Acceder a los valores del diccionario
print(diccionario.values())

##Acceder a las parejas de datos del diccionario
print(diccionario.items())

##Acceder a los valores correspondeintes de cada clave
print(f"La estatura del usuario {diccionario['Nombre']}, es {diccionario['Estatura']} metros")

#Agregar elementos al diccionario

print("\nAgregamos la clave Email: ")
diccionario['Email'] = "cerino@tec.mx" #Sintáxis para agregar una nueva clave
print("Diccionario con una nueva clave: ", diccionario)

##No repetir claves en el diccionario, porque sobreescribe el valor
diccionario['Email'] = "rigo@gmail.com" #Sintáxis para agregar una nueva clave
print("Diccionario con una nueva clave: ", diccionario)

print("\nActualización de los valores de una clave (estatura):")
diccionario["Estatura"] = 1.80
print("Estatura actualizada: ", diccionario)