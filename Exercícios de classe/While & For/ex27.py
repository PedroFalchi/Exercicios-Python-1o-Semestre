num = int(input('Digite a quantidade de elementos: '))


while( (n <= 0) or (n >= 50) ):
    print('Erro! A quantidade de elementos deve estar entre 1 e 49!')
    n = int(input('Digite a quantidade de elementos: '))


a = 1
b = 2


for i in range(num):
    print(f'{a}/{b}')
    a = a + 1
    b = b + 1