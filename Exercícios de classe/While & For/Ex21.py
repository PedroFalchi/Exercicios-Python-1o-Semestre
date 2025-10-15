''' comentar
i = 1
while(i <= 10):
    print(i)
    i = i + 1 '''

num = int(input('Digite um número para obter a tabuada: '))

while(num <= 0):
    print("Não pode número negativo!")
    num = int(input('Digite um outro numero: '))

for i in range(1, 11, 1):
    print(i)