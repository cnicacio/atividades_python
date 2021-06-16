'''
04 (DESAFIO) Crie um jogo onde o computador vai “pensar” em um número entre
0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, entre os
palpites diga ao jogador se o número do computador é maior ou menor ao que ele
digitou,no final mostre quantos palpites foram necessários para vencer.
'''


from random import randint

n1 = randint(1, 10)
n2 = int(input('Digite um número de 1 a 10: '))
palpites = 0

while n2 > 10 or n2 <= 0:
    n2 = int(input('Valor inválido! Digite um número de 1 a 10: '))

while n2 != n1:
    if n2 < n1:
        n1 = randint(1, 10)
        palpites += 1
        n2 = int(input('Número incorreto! Tente um número maior: '))
    elif n2 > n1:
        n1 = randint(1, 10)
        palpites += 1
        n2 = int(input('Número incorreto! Tente um número menor: '))

palpites += 1
print(f'Parabéns! Você acertou após {palpites} tentativas.')