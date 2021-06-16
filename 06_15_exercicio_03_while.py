'''
03 - Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
(C) Qual é o nome do produto mais barato.
'''


custo_1000 = 0
produtos = []
precos = []

while True:
    nome_produto = str(input('Nome do produto (Digite 0 para finalizar compra): '))
    if nome_produto == '0':
        print('Compra finalizada!')
        break
    produtos.append(nome_produto)
    preco = float(input('Valor do produto: R$ '))
    precos.append(preco)

    if preco > 1000:
        custo_1000 += 1

preco_barato = precos.index(min(precos))
produto_barato = produtos.pop(preco_barato)
custo_total = sum(precos)

print(f'''
O total gasto na compra é R$ {custo_total:.2f}
{custo_1000} produtos custaram mais de R$ 1.000.00
O produto mais barato é {produto_barato}
''')
