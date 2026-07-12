# Exercício 7
# Faça um programa que leia 5 números e informe o maior número.

maior = None

for i in range(1,6):
    numero = float(input(f'Digite o {i}º número: '))

    if maior is None or numero > maior:
        maior = numero

print(f'O maior número é: {maior}')