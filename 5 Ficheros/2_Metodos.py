my_file = open('pimerarchivo.txt', 'r')

print(my_file.encoding) #Devuelve el tipo de codificación del archivo
print(my_file.mode) #Devuelve el modo en que se abrió el archivo

print("\nMétodo read(): ")

#contenido = my_file.read()
#print(contenido)
print(my_file.read(15))

my_file.close()

my_file = open('pimerarchivo.txt', 'r')
print("\nMétodo readline()")
print(my_file.readline())
print("\nMétodo readlines()")
print(my_file.readlines()) #método readlines me devuelve una lista 

if my_file.closed:
    print("El archivo se ha cerrado correctamente")
else:
    print("El archivo permanece abierto")

my_file.close()

if my_file.closed:
    print("El archivo se ha cerrado correctamente")
else:
    print("El archivo permanece abierto")