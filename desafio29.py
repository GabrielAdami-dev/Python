r=float(input('Me diga sua velocidade do seu carro:'))

r1=(r-80)*7

if r<=80:
    print('Ok, está tudo certo pode seguir')
   
else:
    print(f'VOCÊ VAI LEVAR UMA MULTA DE R${r1:.1f}')
    print('Por favor na proxíma matenha cuidado')

