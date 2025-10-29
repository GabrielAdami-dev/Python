#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
#A teacher wants to randomly select one of his four students to erase the board. Write a program that helps him by reading the students' names and writing the chosen one's name on the screen.
import random

r= str(input('Digite nome de um aluno: ' ))

s= str(input('Digite nome de um aluno: ' ))

p= str(input('Digite nome de um aluno: ' ))

k= str(input('Digite nome de um aluno: ' ))

po=[r,s,p,k]

po1=random.choice (po)

print('O aluno escolhido foi {} '.format(po1))






