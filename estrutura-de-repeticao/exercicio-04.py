# Exercício 4
# Supondo que a população de um país A seja da ordem de 80_000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200_000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacao_a = 80000
populacao_b = 200000

taxa_a = 0.03
taxa_b = 0.015

anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    anos += 1

print(f'Números de anos: {anos}')
print(f'População do País A: {int(populacao_a)} habitantes')
print(f'População do País B: {int(populacao_b)} habitantes')