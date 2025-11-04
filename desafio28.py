#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
#Write a program that makes the computer "think" of an integer between 0 and 5 and asks the user to try to guess which number the computer chose. The program should then display whether the user won or lost

import random

print('vou pensar em um número de 0 a 5 tente advinhar')

r=int(input('Digite um número de 0 a 5:'))

l=[0,1,2,3,4,5]

r1=random.choice(l)

print('Carregando...')

if r1==r:
    print('Parabéns você acertou o número')
else:
    print('Tente na proximá vai se consegue')