'''
Utilizando os conceitos de Orientação a Objetos ( vistos na aula
anterior, crie um lançador de dados e moedas em que o usuário deve
escolher o objeto a ser lançado Não esqueça que os lançamentos são
feitos de forma rand ô mica
'''

from random import randint

class Jogo:
    def __init__(self, dado, moeda):
        self.dado = dado
        self.moeda = moeda


    def lanca_dado(self):
        if self.dado == 1:
            self.dado = randint(1,6)
            return f'\nVocê tirou {self.dado}'


    def lanca_moeda(self):
        if self.moeda == 1:
            self.moeda = randint(1,2)
            if self.moeda == 1:
                return '\nVocê tirou cara!'
            else:
                return '\nVocê tirou coroa!'
        else:
            pass


while True:
    jogo = int(input('Qual objeto você quer lançar?\n[1] Dado\n[2] Moeda\n'))
    while jogo < 1 or jogo > 2:
        jogo = int(input('VALOR INVÁLIDO!\nQual objeto você quer lançar?\n[1] Dado\n[2] Moeda\n'))
    if jogo == 1:
        jogada = Jogo(1, 0)
        print(jogada.lanca_dado())
    else:
        jogada = Jogo(0, 1)
        print(jogada.lanca_moeda())
    novamente = str(input('Deseja jogar novamente [S/N]? ')).strip().upper()[0]
    while novamente not in 'SN':
        novamente = str(input('Deseja jogar novamente [S/N]? ')).strip().upper()[0]
    if novamente == 'N':
        break

print('OBRIGADO POR JOGAR!')