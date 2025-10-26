#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
#Write a program that converts a temperature entered in degrees Celsius and converts it to degrees Fahrenheit.
c=float(input('Digite em C° para converter em F:'))

f=(c*1.8)+32

print('Convertendo C° {} para F é de {} F '.format(c,f))