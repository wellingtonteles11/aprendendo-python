
# Output Clear

# Exercício 24
# Faça um programa que calcule o mostre a média aritmética de N notas.

quantidade = int(input('Quantas notas deseja informar? '))

soma = 0

for i in range(1, quantidade + 1):
    nota = float(input(f'Digite a {i}ª nota: '))
    soma += nota

media = soma / quantidade
print(f'Média: {media:.2f}')
