peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros: '))
sexo = input('Digite seu sexo, Masculino ou Feminino: ')
imc = peso / (altura ** 2)
if (sexo == 'Feminino'):
    print('Sexo feminino')
elif (imc < 19):
    print('Abaixo do peso')
elif (imc >= 19 and imc <= 24):
    print('Peso ideal')
else:
    print('Acima do peso')
if (sexo == 'Masculino'):
    print('Sexo masculino')
elif (imc < 20):
    print('Abaixo do peso')
elif (imc >= 20 and imc <= 25):
    print('Peso ideal')
else:
    print('Acima do peso')