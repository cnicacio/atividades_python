'''
1. Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.
{1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}
'''

numero = dict()
quadrado = list()

for i in range(6):
    numero['Numero'] = int(input('Insira um número: '))
    numero['Valor'] = numero['Numero'] ** 2
    quadrado.append(numero.copy())

# print(quadrado)

for n in quadrado:
    print(f'O quadrado de {n["Numero"]} é {n["Valor"]}')