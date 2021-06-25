'''
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

def function(a, b, c):
    sum = a + b + c
    return sum


n1 = int(input('Type the first number (N1): '))
n2 = int(input('Type the second number (N2): '))
n3 = int(input('Type the third number (N3): '))

result = function(n1, n2, n3)

print(f'The sum of {n1}, {n2} and {n3} is {result}')