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
        jogos.sort()
        jogo.append(jogos)
    
for j, n in enumerate(jogo): # enumera os jogos e as listas criadas para cada jogo
    print(f'Jogo {j+1} - {n}')


# from random import randint
# from time import sleep

# apostas = list()
# quant = int(input('Quantos jogos você quer fazer? '))

# for c in range(6):
#     lista_temp = list()
#     num = randint(1,60)
#     if num not in lista_temp:
#         lista_temp.append(num)

#     apostas.append(lista_temp[:])

# print(f'\n----- {quant} jogos sendo sorteados -----\n')

# for i, c in enumerate(apostas):
#     print(f'O {i+1}° jogo sorteado foi: {c}')
#     sleep(1)