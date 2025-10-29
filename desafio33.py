a=int(input('Primeiro valor:'))
b=int(input('Segundo valor:'))
c=int(input('Terceiro valor:'))
  
if b<a and b<c:
    menor=b
    if c<a and c<b:
        menor=c
        maior=a
        if b>a and b>c:
            maior=b
        if c>a and c>b:
            maior=c

        print ('o menor valor digitado foi {}'.input(menor))
        print('O maior valor digitado foi {}'.input(maior))



