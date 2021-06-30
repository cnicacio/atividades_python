'''
02 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
dicionário, incluindo o total de gols feitos durante o campeonato.

Vamos aprimorar o código cadastro de jogador de futebol py que foi
desenvolvido no Code Lab da aula 14 Faça com que o seu código
funcione para vários jogadores incluindo um sistema de visualização de
detalhes de aproveitamento de cada jogador.
'''

class Jogador:
    def __init__(self, nome, partidas, gol):
        self.nome = nome
        self.partidas = partidas
        self.gol = gol
        self.golspart = self.gol / self.partidas

    def jogador(self):
        return {'Nome': self.nome,
        'Partidas': self.partidas,
        'Gols': self.gol,
        'Gols por partida' : self.golspart
        }


while True:
    nome = input('Digite o nome do jogador: ').strip().title()
    partidas = int(input('Digite a quantidade de partidas jogadas: '))
    gol = int(input('Digite a quantidade de gols: '))

    jogador = Jogador(nome, partidas, gol)
    jogador.jogador()

    for k, v in jogador.jogador().items():
        print(f'{k}: {v}')

    novo = str(input('Deseja cadastrar um novo jogador [S/N]? ')).strip().upper()[0]
    while novo not in 'SN':
        novo = str(input('Deseja cadastrar um novo jogador [S/N]? ')).strip().upper()[0]
    if novo == 'N':
        break