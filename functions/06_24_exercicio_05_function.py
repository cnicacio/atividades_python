'''
Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
'''

def imc(weight, height):
    index = weight / ((height/100) ** 2)

    if index < 18.5:
        return f'O IMC é igual a {index:.1f}. Você está abaixo do peso!'
    elif 18.5 <= index < 25.0:
        return f'O IMC é igual a {index:.1f}. Você está no peso ideal!'
    elif 25 <= index < 30:
        return f'O IMC é igual a {index:.1f}. Você está com sobrepeso!'
    elif 30 <= index < 35:
        return f'O IMC é igual a {index:.1f}. Você está com obesidade moderada!'
    elif 35 <= index < 40:
        return f'O IMC é igual a {index:.1f}. Você está com obesidade severa!'
    else:
        return f'O IMC é igual a {index:.1f}. Você está com obesidade mórbida!'

def menu():
    name = str(input('Digite o seu nome: ')).title()
    w = float(input('Digite seu peso em quilogramas: '))
    h = int(input('Digite sua altura em centímetros: '))

    return f'{name}, de acordo com sua altura = {h} e peso = {w}: {imc(w, h)}'
    
print(menu())