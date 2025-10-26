#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#Create an algorithm that reads the price of a product and shows its new price, with a 5% discount.
n=int(input('Digite um valor para receber uma promoção:'))

s=n-(n*5/100)

print('Você digitou R${}, e vai receber 5%, e vai custar com desconto R${} '.format(n,s))
