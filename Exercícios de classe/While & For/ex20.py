i = 1
soma = 0
pos = 0
neg = 0

n = int(input('Digite a quantidade de numeros que serão digitados: '))
while(n <= 0 or n > 20):
    print('Filho, a quantidade deverá ser entre 1 a 20! ')
while (i <= n):
    num = int(input('Digite um número: '))
    if (i == 1):
        maior = num
        menor = num

    soma += num

    if (num > maior):
        maior = num
    if (num < menor):
        menor = num
    if (num >= 0):
        pos +=1
    else:
        neg +=1

    i+=1
media = soma / n
per_neg = (neg * 100) / n
per_pos = (pos * 100) / n

print(f'O maior numero: {maior}')
print(f'O menor numero: {menor}')
print(f'A soma é: {soma}')
print(f'A media é: {media}')
print(f'Porcentagem positiva: {per_pos}')
print(f'Porcentagem negativa: {per_neg}')