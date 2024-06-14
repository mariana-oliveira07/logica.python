sexo = input('Digite seu sexo:')
altura = float(input('Digite sua altura'))
               
if sexo == 'Masculino':
    pesoideal = (72.7*altura)-58
else:
    pesoideal = (62.1*altura)-44.7
    print('Peso ideal', pesoideal)