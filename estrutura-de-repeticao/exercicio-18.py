# Exercício 18
# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

quantidade = int(input('Quantos números você deseja digitar? '))

maior = None
menor = None
soma = 0

for i in range(quantidade):
    numero = int(input(f'Digite o {i + 1}º número '))

    soma += numero

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
print(f'Soma dos números: {soma}')