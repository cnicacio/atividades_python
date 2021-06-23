'''
2. Exercício Treino - Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor associado é o número ao quadrado.
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
'''

numero = dict()
quadrado = list()

for i in range(10):
    numero['Numero'] = i + 1
    numero['Valor'] = numero['Numero'] ** 2
    quadrado.append(numero.copy())

print(quadrado)

for n in quadrado:
    print(f'O quadrado de {n["Numero"]} é {n["Valor"]}')