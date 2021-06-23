'''
04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
Mostre também quantos valores pares foram digitados.
'''


pares = 0

for num in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares += 1

print(f'Você digitou {pares} números pares.')