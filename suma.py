def suma(a:int,b:int):
    return (a+b)

def run():
    print('Este programa suma dos numeros')
    a = int(input('Inserta el primer numero: '))
    b = int(input('Inserta el segundo numero: '))
    print('el resultado es: {}'.format(suma(a,b)))

if __name__ == '__main__':
    repeat=None
    while not repeat:
        run()
        repeat=input('Si quieres realizar otra suma da enter, si no escribe exit: ')