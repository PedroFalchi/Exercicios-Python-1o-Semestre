t = 1
while(t < 21):
    n = 1
    while(n < 11):
        r = t * n
        print(f'{t} x {n} = {r}')
        n = n + 1
    input('Pressione uma tecla para continuar: ')
    t = t + 1



for t in range(1, 21, 1):
    for n in range(1, 11, 1):
        r = t * n
        print(f'{t} x {n} = {r}')
    input('Pressione uma tecla para continuar: ')
