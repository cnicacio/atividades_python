'''
02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
disso, crie duas listas extras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
geradas.
'''

lista = []
lista_par = []
lista_impar = []

while True:
    valor = int(input('Digite um número [Para interromper o programa, digite 9999]: '))
    lista.append(valor)

    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
    
    if valor == 9999:
        print('Preenchimento finalizado!')
        break

del lista[-1]
del lista_impar[-1]

print(f'''
A lista inserida foi {lista}
A lista com os números pares da lista é {lista_par}
A lista com os números ímpares da lista é {lista_impar}
''')