# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 4.0: REPROVADO
#Média entre 4.0 e 5.9: RECUPERAÇÃO
#Média 6.0 ou superior: APROVADO
# Create a program that reads two grades from a student and calculates their average, displaying a message at the end according to the average achieved:
#Average below 4.0: FAILED
#Average between 4.0 and 5.9: RECOVERY
#Average 6.0 or higher: PASSED


p=float(input('Primeira nota:'))

o=float(input('Segunda nota:'))

r=(p+o)/(2)


if r>=6:
    print(f'Parabéns você tirou nota {r:.2f} , você passou de ano!')
elif r<4:
   print(f'Infelizmente você tirou  nota {r:.2f} , você não passou de ano!')
elif r>4 and r<5.9:
    print(f'Você quase conseguiu tirou nota {r:.2f} , você tem que fazer recuperaçao ')