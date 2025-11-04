#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior,O segundo valor é maior,Não existe valor maior, os dois são iguais
#Write a program that reads two integers and compares them, displaying the following message on the screen:
#"The first value is greater.""The second value is greater.""There is no greater value; they are equal."



r=int(input('Digite o primeiro número:'))

r2=int(input('Digite o segundo núemro:'))

if r<r2 :
    print('O Segundo núemero é maior!')
elif r>r2:
    print('O Primeiro número é maior!')
elif r2==r:
    print('Os dois número são iguais!')
  
   