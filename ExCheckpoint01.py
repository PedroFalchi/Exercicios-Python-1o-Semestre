peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros: '))
sexo = input('Digite seu sexo, Masculino ou Feminino: ')
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.2f}')
if (sexo == 'Feminino'):
    print('Sexo feminino')
    if (imc < 19):
        print('Abaixo do peso')
    elif (imc >= 19 and imc <= 24):
        print('Peso ideal')
    else:
        print('Acima do peso')
elif (sexo == 'Masculino'):
    print('Sexo masculino')
    if (imc < 20):
        print('Abaixo do peso')
    elif (imc >= 20 and imc <= 25):
        print('Peso ideal')
    else:
        print('Acima do peso')
else:
    print('Sexo inválido')