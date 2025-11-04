#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#Write a program that reads a young person's birth year and, based on their age, indicates whether they are still going to register for military service, if it's the exact time to register, or if they have already missed the registration deadline. Your program should also show how much time is left or how long it has passed since the deadline.

n=int(input('Seu ano de nascimento? '))

p=(2025-n)

i=18-p
t=i+2025

i2=p-18
t2=2025-i2

if p>18:
    print('Você nasceu em {}, atualmente tem {} anos em 2025'.format(n,p))
    print('Você deveria já deveria ter se alistado a {} anos atrás. \n Seu alistamento foi em {} '.format(i2,t2))
elif p<18:
    print('Você nasceu em {}, atualmente tem {} anos em 2025'.format(n,p))
    print('Você deve voltar daqui a {} anos. \n Seu alistamento vai ser em {}'.format(i,t))
elif p==18:
    print('Você nasceu em {},atualmente tem {} anos em 2025'.format(n,p))
    print('Você deve se Alistar IMEDIATAMENTE!')