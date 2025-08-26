#Solicitar datos al usuario 
#función "input"
#variable = input("Mensaje a presentar al usuario")
'''
vocal = input("Escriba una vocal en mayúsculas: ")

if vocal.upper()== "E":
    print("Has escrito la vocal E")

cadena = input("Inserte un datoalfanumérico: ")
if cadena.isalnum():
    print("El dato es alfanumérico")
else:
    print("El dato no es alfanumérico")
'''

email = input("Inserte su correo electrónico: ")
print(email.find("@"))

#prnt(email.find("@",0, 5)) # buscar caracter entre índices

print(email[6])

if email.find("@") >= 0 and email.find(".") >= 0:
    print("Tu correo electrónico es válido")
    print("Tu correo electrónico es: {}".format(email))
else:
    print("Tu correo electrónico no es válido")


