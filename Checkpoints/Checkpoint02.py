resultado = 0
i = 1
maior = 0

for i in range(1, 11, 1):
    num = int(input(f'Digite o {i} número: '))
    while (num <= 0):
        print('Digite apenas números positivos: ')
        num = int(input(f' Digite o {i} número: '))
    resultado = resultado + num
    
if (num > maior):
    maior = num
    print(f'O maior valor é: {maior}')

soma = resultado
print(f'A soma dos números entre 1 e 10 é: {soma}')

media = soma / 10
print(f'A média dos números é: {media}')