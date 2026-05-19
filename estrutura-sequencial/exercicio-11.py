# Exercício 11
# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

# O produto do dobro do primeiro com metade do segundo .
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.

numero1 = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo número inteiro: '))
numero_real = float(input('Digite um número real: '))

print(f'O produto do dobro do primeiro com metade do segundo: {(numero1 * 2) * (numero2 / 2)} ')
print(f'A soma do triplo do primeiro com o terceiro: {(numero1 * 3) + numero_real}')
print(f'O terceiro elevado ao cubo: {numero_real ** 3}')