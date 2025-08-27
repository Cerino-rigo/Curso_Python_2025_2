with open("Fragmento El Principito.txt", 'r', encoding="utf-8") as file:
    listan = []

    texto = file.read()

    lineas = texto.splitlines() #Devuelve una lista con las líneas del archivo
    print(lineas)
    print("El archivo tiene ", len(lineas), "líneas")

    print(texto.count("de"))
    print("El archivo tiene ", texto.count("de"), "veces la palabra 'de'")

with open("Fragmento El Principito.txt", 'r', encoding="utf-8") as file:
    num = 0 #Inicializar variable num
    for linea in file:
        palabras = linea.split() #Dividimos una cadena
        print(palabras)
        print(len(palabras))
        num += len(palabras) #Acumular valores en la variable num

print(f"El total de palabras en el texto es de: {num}")
