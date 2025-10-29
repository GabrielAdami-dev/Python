#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#Write a program that reads the length of the opposite and adjacent legs of a right triangle. Calculate and display the length of the hypotenuse.

import math

n=float(input('Digite o  Cateto Adjacente: '))

r=float(input("input(Digite o Cateto Oposto: "))

f= (n**2)+(r**2)

print('A sua Hipotenusa deu {:.2f} '.format (math.sqrt (f)))
