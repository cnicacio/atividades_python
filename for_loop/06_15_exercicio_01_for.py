'''
01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
o maior e o menor peso lidos.
'''


pesos = []

for c in range(1,6):
    kg = float(input(f'Digite o peso da pessoa {c}: '))
    pesos.append(kg)

maior = max(pesos)
menor = min(pesos)

print(f'O maior peso é {maior:.1f} kg e o menor peso é {menor:.1f} kg.')