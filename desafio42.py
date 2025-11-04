#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de #mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
#Redo CHALLENGE 035 about triangles, adding the feature to #show what type of triangle will be formed:
#EQUILATERAL: all sides equal
#ISOSCELES: two sides equal, one different
#SCALENE: all sides different

a=float(input('Digite o primeiro segmento:'))
b=float(input('Digite o segundo segmento:'))
c=float(input('Digite o terceiro segmento'))


if a+b>c and c+b>a and c+a>b:
    print('É possivel fazer um triângulo ', end='')
    if a==b and c==a and b==c:
        print('Equilatero ')
    elif a==b or c==a or b==c:
        print('Isósceles')
    elif a!=b and b!=c and c!=a:
        print('Escaleno')
else:
    print('Não é possivél formar um triângulo')



   