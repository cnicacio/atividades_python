'''
6. Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve
receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as situações dos 15 alunos de uma vez só.
'''

from statistics import mean

aluno = dict()
alunos = list() # lista que receberá os dicionários correspondentes a cada aluno inserido
notas = list() # extrair as notas de cada pessoa

for i in range(15):

    aluno['Nome'] = str(input('Digite o nome completo dx alunx: ')).title()

    for n in range(5):
        aluno[f'Nota {n+1}'] = float(input(f'Digite a nota {n+1} dx {aluno["Nome"]}: ')) # gerará as 5 notas do aluno
        notas.append(aluno[f'Nota {n+1}']) # cria uma lista com todas as notas
    
    aluno['Média'] = mean(notas[-5:]) # calcula a média correspondente às 5 notas inseridas para o aluno

    if aluno['Média'] < 5:
        aluno['Situação'] = 'Reprovadx'

    elif 5 <= aluno['Média'] < 7:
        aluno['Situação'] = 'Recuperação'

    else:
        aluno['Situação'] = 'Aprovadx'

    alunos.append(aluno.copy()) # adiciona o dicionário referente a cada aluno na lista "alunos"

for c in alunos:
    print(f'''
    {'-=' * 11}
    Nome do aluno: {c["Nome"]}
    {'-=' * 11}
    Nota 1: {c["Nota 1"]}
    Nota 2: {c["Nota 2"]}
    Nota 3: {c["Nota 3"]}
    Nota 4: {c["Nota 4"]}
    Nota 5: {c["Nota 5"]}
    {'-=' * 11}
    Média: {c["Média"]}
    {'-=' * 11}
    Situação: {c["Situação"]}
    {'-=' * 11}
    ''')