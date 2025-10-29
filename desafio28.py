import random
print('vou pensar em um número de 0 a 5 tente advinhar')
r=int(input('Digite um número de 0 a 5:'))
l=[0,1,2,3,4,5]
r1=random.choice(l)
print('Carregando...')
if r1==r:
    print('Parabéns você acertou o número')
else:
    print('Tente na proximá vai se consegue')