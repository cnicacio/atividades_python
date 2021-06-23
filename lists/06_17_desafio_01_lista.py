'''
Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import sample

jogo = []
n = int(input('Digite o número de jogos desejados: '))

for i in range(n):
    jogos  = sample(range(1,60), 6) # sample define o número de vezes que o número range(1,60) é inserido
    if jogos not in jogo:
        jogo.append(jogos)

for j, n in enumerate(jogo): # para j 
    print(f'Jogo {j+1} - {n}')
   
# sample não permite repetição de valores!!!!!

''' 
ALTERNATIVA

for j in range(n):
    print(f'{j+1}° jogo - {jogo[a]}')
'''
