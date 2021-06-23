'''
03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
maiores.
'''


ano_atual = 2021
maior_idade = 0
menor_idade = 0

for c in range(1,8):
    ano_nasc = int(input(f'Informe o ano de nascimento da pessoa {c}: '))
    if (ano_atual - ano_nasc) >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

print(f'''
{maior_idade} pessoas são maiores de idade
{menor_idade} pessoas são menores de idade.
''')