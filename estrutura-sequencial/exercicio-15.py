# Exercício 15
# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

ganho_por_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = int(input('Quantas horas você trabalhou no mês? '))

salario_bruto = ganho_por_hora * horas_trabalhadas

imposto_de_renda = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100

total_de_descontos = imposto_de_renda + inss + sindicato

salario_liquido = salario_bruto - total_de_descontos

print(f'O salário bruto é: R$ {salario_bruto:.2f}')
print(f'Desconto do Imposto de Renda (IR 11%): R$ {imposto_de_renda:.2f}')
print(f'Desconto do INSS: R$ {inss:.2f}')
print(f'Desconto do Sindicato: R$ {sindicato:.2f}')
print(f'O salário liquido equivale a: R$ {salario_liquido:.2f}')