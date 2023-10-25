#Lista 4 - Exercício 9

cont = 0
n =  int(input('Informe um número positivo: '))
while n<=0:
    print('Número inválido.')
    n =  int(input('Informe um número positivo: '))
for i in range (1, n+1):
    if n%i==0:
        cont+=1
if cont <= 2:
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')
