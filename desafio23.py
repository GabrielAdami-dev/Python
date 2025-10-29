#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Write a program that reads a number from 0 to 9999 and displays each of the digits separately on the screen.

n=int(input('Digite um número:'))

u= n // 1 % 10

p= n // 10 % 10

o= n // 100 % 10

l= n // 1000 % 10

print(f'Unidade: {u}')

print(f'Decimal: {p}')

print(f'Centena: {o}')

print(f'Milhar: {l}')
