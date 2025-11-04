#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Write a program that reads a person's full name and then displays the first and last names separately.

p=str(input('Digite um nome:')).strip()

o=p.split()

print('Seu primeiro nome é: {}'.format(o[0]))

print('Seu último nome é: {}'.format(o[len(o)-1]))


