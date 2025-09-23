a = float(input('Digite o peso em kg: '))
b = float(input('Digite a altura em metros: '))
x = b / (a * a)
if (x < 20):
    print('Abaixo do peso')
elif (x < 25):
    print('Peso ideal')
else:
    print('Acima do peso')