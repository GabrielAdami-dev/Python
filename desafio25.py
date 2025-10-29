#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#Create a program that reads a person's name and says if they have "SILVA" in their name.
r=str(input('Qual é seu nome completo:')).strip()

print('seu nome é Silva?: {}'.format(r[:5] == 'Silva'))