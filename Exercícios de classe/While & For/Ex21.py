''' comentar
i = 1
while(i <= 10):
    print(i)
    i = i + 1 '''

x = int(input('Digite um número para obter a tabuada: '))


while (x <= 0):
    print('Erro! Digite apenas números positivos!')
    x = int(input('Digite um número para obter a tabuada: '))


a = int(input('Digite o intervalo inicial: '))
b = int(input('Digite o intervalo final: '))


while ( (a <= 0) or (b <= 0) ):
    print('Erro! O intervalo inicial e final devem ser positivos!')
    a = int(input('Digite o intervalo inicial: '))
    b = int(input('Digite o intervalo final: '))


while (b <= a):
    print('Erro! O intervalo final deve ser maior do que o inicial!')
    b = int(input('Digite o intervalo final: '))


while(a <= b):
    r = x * b
    print(f'{x} X {b} = {r}')
    b = b - 1
print('FIM')