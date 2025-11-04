#Exercício Python 041: A Confederação Nacional de Natação #precisa de um programa que leia o ano de nascimento de um #atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
#Python Exercise 041: The National Swimming Confederation #needs a program that reads an athlete's year of birth and displays their category according to age:
#Up to 9 years: MIRIM (Junior)
#Up to 14 years: INFANTIL (Children's)
#Up to 19 years: JÚNIOR (Junior)
#Up to 25 years: SÊNIOR (Senior)
#Over 25 years: MASTER


p=int(input('Digite o ano que você nasceu:'))

p1=2025-p
print('O atleta tem {} anos'.format(p1))

if p1<=9:
    print('Classificação Mirim')
elif p1>=9 and p1<=14:
    print('Classificação Infantil')
elif p1>=14 and p1<=19:
    print('Classificação Júninior')
elif p1>=19 and p1<=25:
    print('Classificação Sênior ')
elif p1>=25:
    print('Classificação  Master')
