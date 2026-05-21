# Exercício 02
# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input('Digite um número: '))

if numero < 0:
    print(f'O número {numero:.0f} é NEGATIVO')
elif numero > 0:
    print(f'O número {numero:.0f} é POSITIVO')

else:
    print(f'O número {numero:.0f} é NEUTRO')

