'''
5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas estão cadastradas.
B) A média da idade.
C) Uma lista com as mulheres.
D) Uma lista com as idades que estão acima da média.
OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.
'''

from statistics import mean

pessoa = dict()
pessoas = list() # lista que receberá os dicionários correspondentes a cada pessoa inserida
feminino = list() # extrair os nomes das pessoas do sexo biológico feminino
idade = list() # extrair as idades de cada pessoa, para facilitar o cálculo da média de idade
acima = list() # extrair as idades das pessoas acima da média de idade

while True:
    pessoa['Nome'] = str(input('Digite o nome da pessoa: ')).title()
    pessoa['Sexo Biológico'] = str(input(f'Digite o sexo biológico de {pessoa["Nome"]} [F/M]: ')).strip().upper()[0]

    while pessoa['Sexo Biológico'] not in 'FM':
        pessoa['Sexo Biológico'] = str(input(f'Digite corretamente o sexo biológico de {["Nome"]} [F/M]: ')).strip().upper()[0]
    if pessoa['Sexo Biológico'] == 'F':
        feminino.append(pessoa['Nome']) # adiciona o nome e o sexo biológico das pessoas de sexo biológico feminino à lista "feminino"
    
    pessoa['Idade'] = int(input(f'Digite a idade de {pessoa["Nome"]}: '))
    idade.append(pessoa['Idade']) # adiciona a idade das pessoas inseridas à lista "idade"

    pessoas.append(pessoa.copy()) # adiciona o dicionário correspondente a cada pessoa inserida à lista "pessoas"
    
    novamente = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while novamente not in 'SN':
        novamente = str(input('Valor inválido! Deseja continuar [S/N]? ')).strip().upper()[0]
    if novamente == 'N':
        break
    
for i in idade: # para cada valor na lista "idade"
    if i > mean(idade): # se o valor for maior que a média de idade calculada
        acima.append(i) # adiciona-se o valor correspondente à lista "acima"

print(f'''
Foram cadastradas {len(pessoas)} pessoas.
A média de idade das pessoas cadastradas é de {mean(idade):.0f} anos.
As mulheres cadastradas foram: {feminino}.
As idades acima da média são: {acima}.
''')