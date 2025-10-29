#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
#The same teacher from challenge 019 wants to randomly select the order in which students will present their work. Write a program that reads the names of the four students and displays the order selected.
import random 

r=str(input('Digite um aluno: '))

p=str(input('Digite um aluno: '))

o=str(input('Digite um aluno: '))

l=str(input('Digite um aluno:' ))

po=[r, p, o, l]

random.shuffle(po)


print('A sequencia de alunos a apresentar vai ser:\n {} '.format(po))