# Exercício 06
# Faça um programa que leia três números e mostre o maior deles:

primeiro_numero = int(input('Informe o primeiro número: '))
segundo_numero = int(input('Informe o segundo número: '))
terceiro_numero = int(input('Informe o terceiro número: '))

if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    print(f'O número {primeiro_numero} é o maior')

elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    print(f'O número {segundo_numero} é o maior')

elif terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero:
    print(f'O número {terceiro_numero} é o maior ')

else:
    print(f'Todos os números são iguais ')