aceleracao = float(input('Digite o valor da aceleração em m/s2: '))
vInicial = float(input('Digite o valor da velocidade inicial em m/s: '))
tempoPercurso = float(input('Digite o valor da velocidade final em m/s: '))
vFinal = vInicial + (aceleracao * tempoPercurso)
print(f'Velocidade final = {vFinal:.2f} m/s')
if (vFinal <= 40):
    print('Veiculo muito lento')
    if (vFinal >= 40 and vFinal <=60):
        print('Velocidade permitida')
    elif (vFinal >=60 and vFinal <=80):
        print('Velocidade de cruzeiro')
    elif (vFinal >= 80 and vFinal <= 120):
        print('Veiculo rápido')
    elif ( vFinal >= 120):
        print('Veiculo muito rápido')
else:
    print('Veiculo desligado')