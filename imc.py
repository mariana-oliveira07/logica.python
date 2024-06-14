altura = float(input('Didite a altura: '))
peso = input('Digite o peso: ')

imc = 0.0
if (imc):
    imc = (72.7*altura)-58
elif(imc):
    imc = (62.1*altura)-44.7

if(imc < 18.5):
    print('Abaixo do peso: ')
elif (imc < 25):
    print('Peso normal:', round(imc, 2))
elif (imc < 30):
    print('Sobrepeso:', round(imc, 2))
elif (imc < 35):
    print('Obsidade Grau 1:', round(imc, 2))
elif (imc < 40):
    print('Obesidade Grau 2:', round(imc, 2))
elif (imc >=40):
    print('Obesidade Grau 3:', round(imc, 2))

