# Exercício 09
# Faça um programa que leia três números e mostre-os em ordem decrescente:

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
terceiro_numero = int(input('Digite o terceiro número: '))

if primeiro_numero >= segundo_numero and primeiro_numero >= terceiro_numero:
    if segundo_numero >= terceiro_numero:
        print(f'Ordem decrescente: {primeiro_numero}, {segundo_numero}, {terceiro_numero}')
    else:
        print(f'Ordem decrescente: {primeiro_numero}, {terceiro_numero}, {segundo_numero}')

elif segundo_numero >= primeiro_numero and segundo_numero >= terceiro_numero:
    if primeiro_numero >= terceiro_numero:
        print(f'Ordem decrescente: {segundo_numero}, {primeiro_numero}, {terceiro_numero}')
    else:
        print(f'Ordem decrescente: {segundo_numero}, {terceiro_numero}, {primeiro_numero}')

else:
    if primeiro_numero >= segundo_numero:
        print(f'Ordem decrescente: {terceiro_numero}, {primeiro_numero}, {segundo_numero}')
    else:
        print(f'Ordem decrescente: {terceiro_numero}, {segundo_numero}, {primeiro_numero}')


