n = int(input('Digite a quantidade de elementos: '))


while( (n <= 0) or (n >= 50) ):
    print('Erro! A quantidade de elementos deve estar entre 1 e 49!')
    n = int(input('Digite a quantidade de elementos: '))


a = 2
b = 1
inc_a = 3
inc_b = 1


for i in range(n):
    print(f'{a}/{b}')
    a = a + inc_a
    inc_a = inc_a + 2
    inc_b = inc_b + 1
    b = (inc_b * inc_b * inc_b)