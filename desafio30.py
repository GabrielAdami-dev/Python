#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
#Write a program that reads an integer and displays on the screen whether it is EVEN or ODD.

p=int(input('Digite qualquer número:'))

r=p%2

if r==0:
   print('O número {} é par'.format(p))
else:
    print('O número {} é ímpar'.format(p))