r=int(input('Qual é a distância da viajem?'))

y=((r-200)*0.45)+(200*0.5)
r1=(r*0.5)

if r <= 200:
    print('A sua viagem deu R$ {}'.format(r1))
else:
    print('A sua viagem deu R$ {}'.format(y))
    