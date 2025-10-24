maior = 0
soma = 0

for i in range (1, 11, 1):
    num = int(input("Digite um número: "))
    while(num <= 0):
        print("Digite apenas números positivos: ")
        num = int(input("Digite um número: "))

    if (num > maior):
        maior = num

    soma = soma + num

media = soma / 10

print(f'O maior valor é: {maior}')
print(f'A soma dos números entre 1 e 10 é: {soma}')
print(f'A média dos números é: {media}')