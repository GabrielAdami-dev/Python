#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#Make a program that reads any angle and displays on the screen the value of the sine, cosine and tangent of that angle.
import math

n=int(input('Dgite seu Ângulo para saber a Sin, Cos e Tan : '))

sin=math.sin(math.radians(n))

cos=math.cos(math.radians(n))

tan=math.tan(math.radians(n))

print('Seu ângulo de um Sin de {:.2f} , um Cos de {:.2f} e \n uma Tan de {:.2f} '.format ( sin, cos, tan))