#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
#Make a program that reads something from the keyboard and displays its primitive type and all possible information about it on the screen.
r=(input('Digite algo:'))

print('o valor é uma letra?',r.isalpha())

print('o valor é um espaço?',r.isspace())

print('o valor é um número?',r.isnumeric())

print('o valor é um alfa númerico?',r.isalnum())

print('o valor é uma letra maiúscula?',r.isupper())

print('o valo é uam letra minúscula?:',r.islower())

print('o valo é capitalizado?:',r.istitle())

n=(input('Digite algo e descubra o valo primitivo:'))

print('o valo promitivo dele é',type(n))

print('ele é um número',n.isnumeric())






