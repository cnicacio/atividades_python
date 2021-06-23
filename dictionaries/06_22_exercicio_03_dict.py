'''
3. Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.
'''

aluno = dict()

aluno['Nome'] = str(input('Digite o nome completo do aluno: ')).title()
aluno['Média'] = float(input(f'Digite a média de {aluno["Nome"]}: '))

if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'

elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'

else:
    aluno['Situação'] = 'Aprovado'

print(f'''Aluno: {aluno["Nome"]}
Média: {aluno["Média"]}
Situação: {aluno["Situação"]}
    ''')