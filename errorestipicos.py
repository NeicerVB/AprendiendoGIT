# El error tipico al abrir un archivo sin el with es no cerrarlo
file = open('./Carta.txt', 'r+')
file.read() # Lee el archivo
file.close() # cierra el archivo