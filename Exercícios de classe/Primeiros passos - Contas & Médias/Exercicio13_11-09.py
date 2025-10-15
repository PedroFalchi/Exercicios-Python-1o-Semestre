a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
if (a > b) and (a > c):
    print(f'O maior valor é o {a}')
elif (b > a) and (b > c):
    print(f'O maior valor é o {b}')
else:
    print(f'O maior valor é o {c}')