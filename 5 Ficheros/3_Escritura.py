print("Abrir archivo en modo escritura, al final del archivo")

my_file = open('pimerarchivo.txt', 'a')

print("\nMétodo writable" )
print(my_file.writable())

#Agregar datos al final del documento
my_file.write("\nEsta es una historia nunca antes contada.")

my_file.close()

my_file = open('pimerarchivo.txt', 'r')
print(my_file.read())