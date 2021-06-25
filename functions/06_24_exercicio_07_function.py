'''
Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.
'''

def numbers(a, b):
    if a < b:
        return f'O menor número é {a:.0f}'
    elif b < a:
        return f'O menor número é {b:.0f}'
    else:
        return f'{a:.0f} e {b:.0f} são iguais'

def menu():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    return(f'''
    Primeiro número: {n1:.0f}
    Segundo número: {n2:.0f}
    {numbers(n1, n2)}
    ''')

print(menu())