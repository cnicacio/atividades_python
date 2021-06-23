'''
4. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
'''

from datetime import datetime

pessoa = {}
ano_atual = datetime.now().year

pessoa['Nome'] = str(input('Digite o nome completo da pessoa: ')).title()
pessoa['Ano de Nascimento'] = int(input(f'Digite o ano de nascimento de {pessoa["Nome"]}: '))
pessoa['Idade'] = ano_atual - pessoa['Ano de Nascimento']
pessoa['CTPS'] = int(input('Digite somente os números de sua CTPS: '))

if pessoa['CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input('Digite o ano de contratação: '))
    pessoa['Salário'] = float(input('Digite o salário: '))
    pessoa['Idade de aposentadoria'] = pessoa['Idade'] + (35 - (ano_atual - pessoa['Ano de contratação']))

print(pessoa)