'''
DESAFIO - Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.
'''

def date(d, m, y):
    from datetime import date
    month = date(1900, m, 1).strftime('%B')
    return f'{y}, {month} {d}'

def menu():
    while True:
        dd = int(input('Type the day: '))
        mm = int(input('Type the month: '))
        yyyy = int(input('Type the year: '))
        return date(dd, mm, yyyy)

print(menu())