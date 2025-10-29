r=float(input('Coloque seu salario para ver quanto de aumento irá receber:'))
r1=(r*0.10)+r
r2=(r*0.15)+r
if r>=1250:
    print('Você recebeu um aumento de 10%, agora receberá R${}'.format(r1))
else:
    print('Você recebeuy um aumento de 15%, agora receberá R$ {}'.format(r2))