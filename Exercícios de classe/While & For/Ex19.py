num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o primeiro numero: "))
num3 = int(input("Digite o primeiro numero: "))
num4 = int(input("Digite o primeiro numero: "))
num5 = int(input("Digite o segundo numero: "))

if (num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5):
    print(f'O maior número é: {num1}')
elif (num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5):
    print(f'O maior número é: {num2}')
elif (num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5):
    print(f'O maior número é: {num3}')
elif (num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5):
    print(f'O maior número é: {num4}')
else:
    print(f'O maior número é: {num5}')

if (num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5):
    print(f'O menor número é: {num1}')
elif (num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5):
    print(f'O menor número é: {num2}')
elif (num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5):
    print(f'O menor número é: {num3}')
elif (num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5):
    print(f'O menor número é: {num4}')
else:
    print(f'O menor número é: {num5}')

soma = num1 + num2 + num3 + num4 + num5
print(f'A soma dos números é: {soma}')

mediaArit = soma / 5
print(f'A média aritmética dos números é: {mediaArit}')

per_neg = (soma * 100 / 5)
print(f'A porcentagem de números negativos é: {per_neg}%')

per_pos = (soma * 100 / 5)
<<<<<<< HEAD:Ex19.py
print(f'A porcentagem de números positivos é: {per_pos}%')
=======
print(f'A porcentagem de números positivos é: {per_pos}%')
>>>>>>> 513a2aa0d28f3c637da7c043f40a975b317e4d4f:Exercícios de classe/While & For/Ex19.py
