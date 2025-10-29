

p=str(input('Digite uma Palavra:')).strip()

t=p.upper()
l=t.count('A')
print('A letra A aparece {}'.format(l))

j=t.find('A')+1

print('A primeira letra A aparece na posição {}'.format(j))

u=t.rfind('A')-p.count(' ')+1

print('A última letra A aparece na posição {} '.format(u))


