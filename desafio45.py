from random import choice
print('''Escolha uma das opções:
      [0]Tesoura
      [1]Papel
      [2]Pedra''')
r=int(input('Escolha uma opção:'))

t=('Tesoura')
y=('Papel')
u=('Pedra')
o=[t,y,u]
k=choice(o)

print('O jogador jogou {}'.format(o[r]))
print('computador jogou {}'.format(k))

if k == t:
      if r==0:
       print('Deu empate')
      elif r==1:
       print('O compuatdor venceu')
      elif r==2:
            print('O jogador venceu')
      else:
          print('Jogada invalida')
elif k == y:
      if r==0:
            print('O jogador venceu')
      elif r==1:
          print('Deu empate')
      elif r==2:
          print('O computador venceu')
      else:
          print('Jogada invalida')
elif k == u:
      if r==0:
        print('O computador venceu')
      elif r==1:
       print('O jogador venceu')
      elif r==2:
       print('Deu empate')
      else:
        print('Jogada invalida')


      