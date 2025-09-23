a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
if ( (a+b > c) and (a+c > b) and (b+c > a) ):
  print('Pode formar um triangulo!')

  if ( a == b == c ):
    print('É um triangulo equilátero')
  elif (a != b and a != c and b != c):
    print('É um triangulo escaleno')
  else :
    print('É um triangulo isósceles')

else :
  print('Não é um triangulo!')