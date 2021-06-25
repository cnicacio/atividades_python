'''
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''

def sum_tax(tax, cost):
    tax_calc = cost * (1 + tax/100)
    return tax_calc


cost1 = float(input('Please, type the cost($): '))
tax1 = float(input('Please, type the tax (%): '))

print(f'The item costing {cost1:.2f} with taxes {tax1:.2f} % is $ {sum_tax(tax1, cost1):.2f}')