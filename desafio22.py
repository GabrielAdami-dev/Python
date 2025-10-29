#Crie um programa que leia o nome completo de uma pessoa e mostre: Quantas letras ao todo (sem considerar espaços).Quantas letras tem o primeiro nome.
#Create a program that reads a person's full name and shows: How many letters in total (without considering spaces). How many letters does the first name have.
nome=str(input('Digite seu nome:')).strip()

print('Analisando o seu nome...')

r=nome.upper()

print(f'Seu nome em maiúsculas é: {r}') 

n=nome.lower()

print(f'Seu nome em minúsculas é: {n}')

k=str(len(nome)-nome.count(' '))

print(f'Seu nome tem {k} caracteris')

l=nome.split()

j=len(l[0])

print(f'Seu primeiro nome tem {j} caracteris')

 
 