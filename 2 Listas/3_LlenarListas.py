meses_vendidos = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
ventas = [1200, 1450, 980, 1780, 1350]

total_ventas = sum(ventas)
promedio_ventas = total_ventas / len(ventas)
print(f"El promedio de ventas es: ${promedio_ventas}")

mejor_mes_indice = ventas.index(max(ventas))
mejor_mes = meses_vendidos[mejor_mes_indice]

print(f"Mejor mes: {mejor_mes} con ${max(ventas)}")

##Llenar una lista
listav = [] #Crear lista vacía
print(type(listav))

edad = int(input("Ingresa tu edad: "))
#Método para llenar una lista
listav.append(edad)
print("La edad del usuario es: ", listav)
print("La edad del usuario es: ", listav[0])