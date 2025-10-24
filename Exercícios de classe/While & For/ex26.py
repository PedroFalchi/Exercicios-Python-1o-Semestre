n = int(input('Digite a quantidade de elementos: '))


while( (n <= 0) or (n >= 100) ):
    print('Erro! A quantidade de elementos deve estar entre 1 e 99!')
    n = int(input('Digite a quantidade de elementos: '))


s = 2
c = 3


for i in range(n):
    print(s)
    s = s + c
    c = c + 2