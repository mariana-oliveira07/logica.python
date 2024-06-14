altura = float(input('Didite a altura: '))
sexo = input('Digite o sexo: ')

if (sexo == 'M'):
    pesoIdeal = (72.7*altura)-58
else:
    pesoIdeal = (62.1*altura)-44.7

print('Seu peso ideal é:', pesoIdeal)