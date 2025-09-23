a = float(input('Digite o valor da base do triangulo: '))
b = float(input('Digite o valor da altura do triangulo: '))
x = (a * b) / 2
if (x >= 100):
    print(f'Terreno grande.')
else:
    print(f'Terreno pequeno.')