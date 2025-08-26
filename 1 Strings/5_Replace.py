mensaje = """
Disfruto programar en C++
C++ es fácil de aprender
Llevo programando C++ más de 2 años
"""
print(mensaje)

mensaje_nuevo = mensaje.replace("C++", "Python")
print("Mensaje nuevo: ", mensaje_nuevo)

mensaje2 = "El lunes es el primer día de la semana. El lunes es muy productivo. Los lunes se entregan tareas"
#cadena.replace("this_string", "other_string", n_veces)
print(mensaje2.replace("lunes", "viernes",1))