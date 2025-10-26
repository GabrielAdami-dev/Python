# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy.
n=float(input('Digite um valor de R$ para converter a US$:'))

s=(n/5.39) 

print('A sua conversão de R$ {} deu US$ {}'.format(n,s))