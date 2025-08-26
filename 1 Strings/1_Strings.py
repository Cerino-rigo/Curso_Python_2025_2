#Declarar una variable tipo string, se escribe entre ""
cadena = "Esto es un ejemplo de cadena de texto"
print(cadena)
print(type(cadena))

cadena1 = 'Ejemplo de "cadena" con comillas simples'
print(cadena1)

cadena_triple = """
Esto es un ejemplo de cadena con:
comillas triples.
Adios.
"""
print(cadena_triple)

#Salto de línea en cadenas
cadena2 = "Esto es \n otro ejemplo de una cadena"
print(cadena2)

cadena3 = "Esto es \t otro ejemplo de una cadena"
print(cadena3)

## Escapar o saltar caracteres
cadena4 = "Un salto de línea en python se realiza con \\n"
print(cadena4)

nombre = "Hola Rigo"
apellido = "Cerino"
edad = 28

#Sumar una cadena. Conocido como concatenación de cadenas 
print(nombre + apellido)
print(nombre, apellido)

#Multiplicar una cadea
print(nombre*4)

print("Hola usuario: " + apellido)

numero = 30.5
numero2 = "35.5"
numero3 = int(numero)
#print(numero + numero2)
print(numero3)

#Casteo / casting de una variable
print(numero + numero3)
#print(numero +int(numero2))
