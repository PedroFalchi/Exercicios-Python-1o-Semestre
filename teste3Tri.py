a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

if ( a + b > c) or (a + c > b) or (b + c > a):
    print('É um triangulo')
    if (a == b == c):
        print('É um triangulo equilátero')
    elif (a == b) or (a == c) or (b == c):
        print('É um triangulo isósceles')
    elif (a != b != c):
        print('É um triangulo escaleno')
    else:
        print('Não é um triangulo')