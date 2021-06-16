'''
01 - Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
sem break)
'''


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    opcao = int(input('''
Digite uma das opções abaixo:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
'''))
    if opcao == 1:
        print(f'A soma de {n1} e {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'A multiplicação de {n1} e {n2} = {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n1 < n2:
            print(f'{n2} é maior que {n1}')
        else:
            print(f'{n1} é igual a {n2}')
    elif opcao == 4:
        n1 = int(input('Digite novamente o primeiro número: '))
        n2 = int(input('Digite novamente o segundo número: '))
    elif opcao == 5:
        print('Programa encerrado!')
