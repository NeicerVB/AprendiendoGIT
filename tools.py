print('Estoy aprendiendo muy rápido 😎')

x = 1
def too():
    print(x.is_integer())

def too1():
    '''
    El operador de asignación +=
    trabaja en un área local y no
    de manera global
    '''
    x+=1
    print(x)

too()
too1()