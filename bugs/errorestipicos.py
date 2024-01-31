# El error tipico al abrir un archivo sin el with es no cerrarlo
file = open('./Carta.txt', 'r+')
file.read() # Lee el archivo
file.close() # cierra el archivo

# Error tipico, los elementos de un strin son inmutables
nombre = input('Ingrese su nombre: ')
nombre[0] = 'e'
print(nombre)