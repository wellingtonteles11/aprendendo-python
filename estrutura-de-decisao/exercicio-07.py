# Exercício 07
# Faça um programa que leia três números e mostre o maior e o menor deles:

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
terceiro_numero = int(input('Digite o terceiro número: '))

if primeiro_numero == segundo_numero == terceiro_numero:
    print('Todos os números são iguais')

else:
    maior_numero = max(primeiro_numero, segundo_numero, terceiro_numero)
    menor_numero = min(primeiro_numero, segundo_numero, terceiro_numero)
    
    print(f'O maior número é {maior_numero} e o menor numero é {menor_numero}')
