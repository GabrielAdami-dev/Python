#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
#Write a program that asks an employee for their salary and calculates the amount of their raise. For salaries above R$1250.00, calculate a 10% raise. For salaries equal to or below this amount, calculate a 15% raise.

r=float(input('Coloque seu salario para ver quanto de aumento irá receber:'))

r1=(r*0.10)+r

r2=(r*0.15)+r

if r>=1250:
    print('Você recebeu um aumento de 10%, agora receberá R${}'.format(r1))
else:
    print('Você recebeu um aumento de 15%, agora receberá R$ {}'.format(r2))