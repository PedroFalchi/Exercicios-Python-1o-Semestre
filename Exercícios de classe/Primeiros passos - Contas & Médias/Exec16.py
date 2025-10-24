a = float(input('Digite o primeiro lado do triangulo: '))
b = float(input('Digite o segundo lado do triangulo: '))
c = float(input('Digite o terceiro lado do triangulo: '))
 
if ( (a*a) == ((b*b)+(c*c)) ):
    print('É um triângulo retângulo')
else:
    print('Não é um triângulo retângulo')