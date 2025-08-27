ruta = "segundo_archivo.txt"

with open(ruta, mode = "w", encoding="utf-8") as fichero:
    print("Bienvenidos! A este segundo archivo de texto creado desde la plataforma VS Code a partir de código python", file=fichero)
    print("Bienvenidos! A este segundo archivo de texto creado desde la plataforma VS Code a partir de código python 2", file=fichero)
    print("Bienvenidos! A este segundo archivo de texto creado desde la plataforma VS Code a partir de código python 3", file=fichero)

if fichero.closed:
    print("El archivo se ha cerrado correctamente")
else:
    print("El archivo permanece abierto")

with open(ruta, "r") as file: 
    # Leer el archivo línea por línea
    print("Contenido del archivo: ")
    for line in file:
        print(line)

with open(ruta, "r") as file: 
    lineas = file.readlines() #Leer todas las líneas en una sola ejecución
    print("Líneas del archivo: ", lineas) #Devuelve una lista con las líneas
    print("El archivo tiene", len(lineas), "líneas")

    j = 0
    for i in lineas:
        print(f"Línea {j+1}:", lineas[j], end='') #Cominllas simples: salto de línea
        j += 1