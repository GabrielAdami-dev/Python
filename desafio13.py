#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
#Make an algorithm that reads an employee's salary and shows their new salary, with a 15% increase.
n=float(input('Qual salario do funcionario:'))

r=n+(n*15/100)

print('O funcionario ganhava R$ {}, agora começou a ganhar com aumento de 5%,R$ {}'.format(n,r))