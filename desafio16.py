#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Create a program that reads any Real number from the keyboard and displays its Integer portion on the screen.

import math 

n=float(input('Digite um número: '))

r=math.floor(n)

print('Seu número arrendodado é {}'.format(r))


