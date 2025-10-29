#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
#Create a program that reads the name of a city and says whether or not it starts with the name "SANTO".
r=str(input('Digite o nome de sua cidade:')).strip()

print(r[:5] == 'Santo')

