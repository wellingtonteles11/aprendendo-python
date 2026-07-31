# Exercício 28
# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade_cds = int(input('Quantos CDs o colecionador possui? '))

total = 0

for i in range(1, quantidade_cds + 1):
    valor_cd = float(input(f'Qual o valor do {i}º CD ? '))
    total += valor_cd

media = total / quantidade_cds
print(f'O valor médio gasto em CDs é: R$ {media:.2f}')
print(f'O valor total investido foi: R$ {total:.2f}')