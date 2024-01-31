# El error tipico al abrir un archivo sin el with es no cerrarlo
#file = open('./Carta.txt', 'r+')
#file.read() # Lee el archivo
#file.close() # cierra el archivo

# Error tipico, los elementos de un strin son inmutables
nombre = list(input('Ingrese su nombre: '))
nombre[0] = 'e'
nombre = "".join(i for i in nombre)
print(nombre)