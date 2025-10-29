print('Seguimento de triângulos')

r=float(input('Digite o primeiro:'))
p=float(input('Digite o segundo:'))
l=float(input('Digite o terceiro:'))

if r+p>l and l+r>p  and l+p>r:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')