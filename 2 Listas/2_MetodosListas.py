calificaciones = [4, 5, 3, 4, 2, 5, 4, 3, 1, 3]
print(calificaciones)

#Agregar elementos a la lista
calificaciones.append(5)
print("Calificaciones actualizadas: ", calificaciones)

calificaciones.insert(3,5)
print(calificaciones)

calificaciones.insert(-2,4)
print(calificaciones)

#Método count, cuenta cuántas veces se repite el parámetro
productos_5_estrellas = calificaciones.count(5)
print(f"Productos con 5 estrellas: {productos_5_estrellas} productos")

#Método index, devuelve la posición del primer elemnto que coincida con la búsqueda
posicion_primera_mala = calificaciones.index(1)
print(f"Primera calificación baja está en la posición: {posicion_primera_mala}")

#Método sort -Análisis ordenado
calificaciones_copia = calificaciones.copy() #copiar lista
calificaciones_copia.sort() #Ordenar lista de manera ascendente
print(f"Calificaciones ordenadas: {calificaciones_copia}")

calificaciones_copia.reverse() #Ordenar lista de manera descendente
print(f"Calificaciones ordenadas descendente: {calificaciones_copia}")

#Eliminar elementos de una lista
print(calificaciones)
calificaciones.pop(1) #Si tiene argumetos, elimina el valor en esa posición
print("Después de utilizar el método pop: ", calificaciones)

calificaciones.remove(5) #Elimina por valor, no por posición
print("Eliminar con método remove(): ", calificaciones)

# Métodos in / not in
titulo = ['t','u','t','o','r','i','a','l']

if 't' in titulo:
    n = titulo.count('t')
    print(f"\nLa letra 't' se repite {n} veces")
else:
    print("La lista no tiene un elemento con valor 't'")

if 'p' not in titulo:
    print("La lista no tiene un elemento con valor 'p'")
else:
    print("La lista tiene un elemento con el valor 'p'")
