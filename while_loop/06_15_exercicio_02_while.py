'''
02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
'''


maiores_idade = 0
homens = 0
mulheres_menor_20 = 0

while True:
    pessoa = input('Digite o nome da pessoa (Digite 0 para interromper cadastro): ')
    if pessoa == '0':
        print('Cadastro interrompido!')
        break
    sexo_bio = str(input('Digite o sexo biológico da pessoa: ').strip().upper()[0])
    while sexo_bio not in 'FM':
        sexo_bio = str(input('Digite corretamente o sexo biológico da pessoa: ').strip().upper()[0])
    idade = int(input('Digite a idade da pessoa: '))
    if sexo_bio == 'M':
        homens += 1
    if idade > 18:
        maiores_idade += 1
    if sexo_bio == 'F' and idade < 20:
        mulheres_menor_20 += 1

print(f'''
O número de pessoas maiores de 18 anos é {maiores_idade}
O número de homens é {homens}
O número de mulheres menores de 20 anos é {mulheres_menor_20}
''')