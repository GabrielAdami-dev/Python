#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
#Write a program that reads a sentence from the keyboard and displays how many times the letter "A" appears, its first position, and its last position
p=str(input('Digite uma Palavra:')).strip()

t=p.upper()
l=t.count('A')
print('A letra A aparece {}'.format(l))

j=t.find('A')+1

print('A primeira letra A aparece na posição {}'.format(j))

u=t.rfind('A')-p.count(' ')+1

print('A última letra A aparece na posição {} '.format(u))


