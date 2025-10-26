#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
#Write a program that asks for the number of kilometers traveled by a rental car and the number of days it was rented. Calculate the price to pay, knowing that the car costs R$60 per day and R$0.15 per kilometer driven.
p=float(input('Quantos dias?:'))

k=float(input('quantos Km rodados?:'))

kp=(60*p)+(0.15*k)

print('O total a pagar é de R$ {}'.format(kp))