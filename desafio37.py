#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
#Write a Python program that reads any integer and asks the user to choose the conversion base: 1 for binary, 2 for octal, and 3 for hexadecimal.


t=int(input('Digite um número:'))

print('''Escolha um para converter:
[ 1 ] Converter para binario:
[ 2 ] Converter para octal:
[ 3 ] Converter para  hexadecimal:''')

r=int(input('escolha uma opção:'))

b=bin(t)[2:]

p=oct(t)[2:]

e=hex(t)[2:]


if r == 1:
    print('Seu número em binario é {}!'.format(b))
elif r == 2:
    print('Seu núemro em octal é {}!'.format(p))
elif r == 3:
    print('Seu núemro em hex é {}!'.format(e))
