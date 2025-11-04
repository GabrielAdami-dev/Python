#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite
#Write a program that reads a car's speed. If it exceeds 80 km/h, display a message saying that a fine has been issued. The fine will cost R$7.00 for each kilometer above the limit.
r=float(input('Me diga sua velocidade do seu carro:'))

r1=(r-80)*7

if r<=80:
    print('Ok, está tudo certo pode seguir')
   
else:
    print(f'VOCÊ VAI LEVAR UMA MULTA DE R${r1:.1f}')
    print('Por favor na proxíma matenha cuidado')

