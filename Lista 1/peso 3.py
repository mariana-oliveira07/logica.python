try:
    altura = float(input('Digite a altura: '))
    sexo = input('Digite o sexo: ')
except Exception as e:
    pesoIdeal = 0.0
    if (sexo.upper() == 'M'): # lower
        pesoIdeal = (72.7*altura)-58
    elif(sexo.upper() == 'F'):
        pesoIdeal = (62.1*altura)-44.7
    else:
        print('O sexo informado deve ser M para masculino ou F par feminino.')

    if(pesoIdeal > 0):
        print('O sexo informado foi: ', sexo.upper())
        print('Seu peso ideal é:', round(pesoIdeal, 2))


    peso = float(input('Digite a peso: '))
    imc = (peso/altura ** 2)
    print('Seu IMC é:', round(imc, 2))

    if (sexo == 'M'):
        imc = (72.7*altura)-58
    elif(sexo == 'F'):
        imc = (62.1*altura)-44.7

    if(imc < 18.5):
        print('Abaixo do peso')
    elif (imc < 25):
        print('Peso normal')
    elif (imc < 30):
        print('Sobrepeso')
    elif (imc < 35):
        print('Obsidade Grau 1')
    elif (imc < 40):
        print('Obesidade Grau 2')
    elif (imc >=40):
        print('Obesidade Grau 3')

