print("""
Manejo de archivos de texto en python y uso de métodos
      -Creación del archivo: 'primerarchivo.txt'
      -Abrir archivo en modo lectura
"""    
)

#Crear un archivo con modo escritura 'w'
my_file = open('pimerarchivo.txt', 'w')

print("\nAquí utilizamos el método write(): ")

my_file.write("Bienvenidos! A este primer archivo de texto creado desde la plataforma VS Code con Python")
my_file.write("\nEste archivo será entretenido, pues aquí, contaremos historias...")
my_file.write("\nComencemos")

#Es una buena práctica de programación cerrar el archivo, utilizamos el método close()
my_file.close()

#Abrir el archivo en modo lectura
print("\nAbrir el archivo en modo lectura")

my_file = open('pimerarchivo.txt', 'r')
print(type(my_file))

#Imprimir el texto
print("\nTexto del documento: ")
print(my_file.read())
my_file.close()