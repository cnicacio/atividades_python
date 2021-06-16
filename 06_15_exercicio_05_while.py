'''
05 (DESAFIO) Em uma eleição presidencial existem quatro candidatos. Os votos
são informados por meio de código.
Os códigos utilizados são:
1 , 2, 3 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - José / 2- João / etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos.
'''


print('''
ELEIÇÕES 2021:

Tabela de candidatos:

===================
Número    Candidato
===================
  1         João
  2         Maria
  3         José
  4         Lúcia
  5         Nulo
  6         Branco
===================
''')

Joao = Maria = Jose = Lucia = Nulo = Branco = 0

while True:
    voto = int(input('Insira o número do seu candidato: '))
    if voto == 0:
        print('Votação encerrada!')
        break
    while voto < 1 or voto > 6:
        voto = int(input('Insira corretamente o número do seu candidato: '))
    if voto == 1:
        Joao += 1
    if voto == 2:
        Maria += 1
    if voto == 3:
        Jose += 1
    if voto == 4:
        Lucia += 1
    if voto == 5:
        Nulo += 1
    if voto == 6:
        Branco += 1

lista_votos = [Joao, Maria, Jose, Lucia, Nulo, Branco]
total_votos = sum(lista_votos)

nulos = (Nulo / total_votos) * 100
brancos = (Branco / total_votos) * 100

print(f'''
RESULTADO - ELEIÇÕES 2021:

João: {Joao} votos
Maria: {Maria} votos
José: {Jose} votos
Lúcia: {Lucia} votos
Nulos: {Nulo} votos
Brancos: {Branco} votos

Relação de votos nulos sobre o total de votos: {nulos:.2f}%
Relação de votos brancos sobre o total de votos: {brancos:.2f}%
''')