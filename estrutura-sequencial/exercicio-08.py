# Exercício 08
# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Quanto você ganha por hora? '))
hora_trabalhada = float(input('Informe quantas horas você trabalhou no mês: '))

salario = valor_hora * hora_trabalhada
print(f'O salário do mês do funcionário é: {salario:.2f}R$')