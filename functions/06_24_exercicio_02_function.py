'''
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.
'''

def number(a):
    if a > 0:
        return f'{a} = Positive'
    elif a < 0:
        return f'{a} = Negative'
    else:
        return f'{a} = 0'


num = int(input('Type a number: '))

print(number(num))