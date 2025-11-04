# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#Develop a program that reads the lengths of three lines and tells the user whether or not they can form a triangle.

print('Seguimento de triângulos')

r=float(input('Digite o primeiro:'))

p=float(input('Digite o segundo:'))

l=float(input('Digite o terceiro:'))

if r+p>l and l+r>p  and l+p>r:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')