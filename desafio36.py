#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
#Write a program to cancel a bank loan for the purchase of a house. Ask for the value of the house, the buyer's salary, and the number of years they will pay it off. The monthly payment cannot exceed 30% of the salary, otherwise the loan will be denied.

p=int(input('Digite o valor da casa: '))

o=int(input('Quanto que você ganha? '))

k=int(input('Em quantos anos você irá pagar?'))

j=(o*0.30)

h=j*(k*12)

if h>=p:
    print('A sua casa de valor de R${}, com {} anos, com uma prestacão mensal R${:.2},até o final resultando em um valor de {:.2} será suficinete para paga-lá'.format(p,k,j,h))
elif h<=p:
    print('A sua casa deu um valor de R${},com {} anos, com uma prestação mensal R${:.2}, seu pobre imundo por que acha que vai comprar está casa de R${:.2}, com uma marrequinha de R${} sai daqui seu imundo!'.format(p,k,j,p,o))
