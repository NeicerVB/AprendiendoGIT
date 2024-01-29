# file = open('test.txt')
# print(file.read())
# file.close()

print({1,2} & {2,4})
# 0001
# 0010
# 0000
names = {'Nicolas', 'Miguel', 'Juan', 'Nicolas'} 
print(names)

with open('./practica/test.txt', 'a+') as file:
    file.write('Hola Python, aun te recuerdo\n')
    file.seek(0)
    print(file.read())