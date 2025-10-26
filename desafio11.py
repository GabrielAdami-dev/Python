#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
#Make a program that reads the width and height of a wall in meters, calculates its area and the amount of paint needed to paint it, knowing that each liter of paint paints an area of ​​2 square meters.
n=float(input('Digite a largura da sua parede:'))

n1=float(input('digite a altura da sua parede:'))

r=n*n1

print('A largura da sua parede é {},e a altura é {}, dando uma área de {}m²,\n para pintar sua parede será necessario {}l de tinta!'.format(n,n1,r,r/10))