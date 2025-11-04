n=float(input('Preço das compras:'))

print('''Escolha a forma de pagamento:
      [1]á Dinheiro/Cheque
      [2]á Vista Cartão
      [3]2x no cartão
      [4]3x ou mais no cartão''')

r=int(input('Escolha uma opção:'))



if r==1:
        print('No Dinheiro/Cheque vai ter um desconto de 10%, e vai ficar R${}'.format(n-(n*0.10)))
elif r==2:
    print('No Cartão á Vista vai ter um desconto de 5%, e vai ficar R${} '.format(n-(n*0.05)))
elif r==3:
    print('Em 2x no Cartão deu R${}'.format(n/2))
elif r==4:
     t=float(input('Quantas parcelas?'))
     p=n*0.20*t
     o=p/t
     print('Sua compra será parcelada em {}x de R${} Com Juros de 20%.\n Sua compra de R${} vai ficar agora R${} '.format(t,o,n,p))

