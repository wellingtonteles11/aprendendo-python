# Exercício 17
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

area_em_metros = float(input('Informe a área a ser pintada em m²: '))

quantidade_litros = (area_em_metros / 6) * 1.10

quantidade_latas = math.ceil(quantidade_litros / 18)
custos_latas = quantidade_latas * 80

galoes_menores = math.ceil(quantidade_litros / 3.6)
custo_galoes = galoes_menores * 25

latas_misturas = int(quantidade_litros // 18)
resto = quantidade_litros - (latas_misturas * 18)

galoes_misturas = math.ceil(resto / 3.6)
preco_misturas = (latas_misturas * 80) + (galoes_misturas * 25)

print('---APENAS LATAS DE 18L---')
print(f'A quantidade de latas é: {quantidade_latas}')
print(f'Preço: R$ {custos_latas:.2f}')

print('---APENAS GALÕES DE 3,6L---')
print(f'A quantidade de galões é: {galoes_menores}')
print(f'Preço: R$ {custo_galoes:.2f}')

print('---MISTURAS DE LATAS E GALÕES---')
print(f'Latas: {latas_misturas}')
print(f'Galões: {galoes_misturas}')
print(f'Preço: R$ {preco_misturas:.2f}')







