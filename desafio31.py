#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas
#Develop a program that asks for the distance of a trip in kilometers. Calculate the fare, charging R$0.50 per kilometer for trips up to 200 km and R$0.45 for longer trips.

r=int(input('Qual é a distância da viajem?'))

y=((r-200)*0.45)+(200*0.5)

r1=(r*0.5)

if r <= 200:
    print('A sua viagem deu R$ {}'.format(r1))
else:
    print('A sua viagem deu R$ {}'.format(y))
    