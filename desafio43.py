p=float(input('Digite seu peso em Kg:'))
a=float(input('Digite sua altura em metros:'))

imc=p/(a*a)

if imc<=18.5:
    print('Abaixo do peso')
elif imc>18.5 and imc<=25:
    print('Peso ideal')
elif imc>=25 and imc<30:
    print('Sobrepeso')
elif imc>=30 and imc<=40:
    print('Já vai te que fazer academia')
elif imc>40:
    print('PARA DE COME MCDONALDS TU VAI MORRER SEU BALOFO')