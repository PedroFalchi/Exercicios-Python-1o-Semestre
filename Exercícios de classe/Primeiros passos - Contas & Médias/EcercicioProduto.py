a = float(input('Digite  o valor do primeiro produto: '))
b = float(input('Digite  o valor do segundo produto: '))
c = float(input('Digite  o valor do terceiro produto: '))
d = float(input('Digite  o valor do quarto produto: '))
e = float(input('Digite  o valor do quinto produto: '))
p = float(input('Digite  o valor do pagamento: '))
x = (a+b+c+d+e)
t = p - x
print(f'O valor do troco é: R$ {t:.2f}')
