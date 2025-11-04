#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#Write a program that reads any given year and determines if it is a leap year.

from datetime import date

a=int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))

if a==0:
    a=date.today().year
if a % 4 == 0 and a % 100!=0 or a % 400 ==0:
    print('O ano {} é Bissexto'.format(a))
else:   
    print('o ano {} não é Bissexto'.format(a))

