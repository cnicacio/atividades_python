'''
Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.
'''

def wage_xyz(value_hour, week_hours):

    if week_hours <= 40:
        wage = value_hour * week_hours
    else:
        wage = (value_hour * 40) + (1.50 * value_hour * (week_hours - 40))
    return wage

def menu():

    worker = str(input('Type the full name of the collaborator: ')).title()
    value = float(input(f'Please, type the wage per hour of {worker} ($): '))
    hour = float(input(f'Please, type the numer of hours worked by {worker} this week: '))
    return f'{worker} has worked {hour:.2f} hours this week. The weekly income is $ {wage_xyz(value,hour):.2f}'

print(menu())