'''
Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).
'''

def grade(g):

    if g >= 9.0:
        return 'A'
    elif 8.0 <= g < 9.0:
        return 'B'
    elif 7.0 <= g < 8.0:
        return 'C'
    elif 6.0 <= g < 7.0:
        return 'D'
    elif 5.0 <= g < 6.0:
        return 'E'
    else:
        return 'F'

def menu():
    name = str(input('Digite o nome dx alunx: ')).title()
    grade_num = float(input('Digite a nota dx alunx: '))
    return f'{name} tirou {grade_num:.2f} na avaliação. Sua nota é {grade(grade_num)}'

print(menu())