'''
02 - Crie um programa que pergunte ao usuário um número inteiro e faça a
tabuada desse número.
'''


numero = int(input('Digite um número: '))

for c in range(1,11):
    print(f'{numero} x {c} = {numero * c}')
