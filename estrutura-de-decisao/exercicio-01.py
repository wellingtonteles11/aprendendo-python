# Exercício 01
# Faça um programa que peça dois números e imprima o maior deles.

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

if primeiro_numero > segundo_numero:
    print(f'{primeiro_numero} é o maior número')

elif primeiro_numero < segundo_numero:
    print(f'{segundo_numero} é o maior número')