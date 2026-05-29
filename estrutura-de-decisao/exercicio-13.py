# Exercício 13
# Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
print('---SELECIONE O DIA---')
print('1 - Domingo')
print('2 - Segunda')
print('3 - Terça')
print('4 - Quarta')
print('5 - Quinta')
print('6 - Sexta')
print('7 - Sábado')
try:
    dia_semana = int(input('Escolha um número correspondente ao dia: '))

    if dia_semana == 1:
        print('Domingo')
    elif dia_semana == 2:
        print('Segunda')
    elif dia_semana == 3:
        print('Terça')
    elif dia_semana == 4:
        print('Quarta')
    elif dia_semana == 5:
        print('Quinta')
    elif dia_semana == 6:
        print('Sexta')
    elif dia_semana == 7:
        print('Sábado')
    else:
        print('COMANDO INVÁLIDO...')

except ValueError:
    print('COMANDO INVÁLIDO...')
