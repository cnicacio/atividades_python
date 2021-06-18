'''
01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente.
'''

lista = []

while True:
    valor = int(input('Digite um número [Para interromper o programa, digite 9999]: '))
    if valor not in lista:
        lista.append(valor)
    
    if valor == 9999:
        print('Preenchimento finalizado!')
        break

del lista[-1]
print(f'A lista de números que você digitou, sem repetições e ordenada é {sorted(lista)}')