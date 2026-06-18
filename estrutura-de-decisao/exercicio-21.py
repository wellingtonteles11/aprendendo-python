# Exercício 21
# Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor = int(input('Digite o valor do saque: R$ '))

if valor < 10 or valor > 600 :
    print('Valor inválido!')
else:
    nota100 = valor // 100
    valor %= 100

    nota50 = valor // 50
    valor %= 50

    nota10 = valor // 10
    valor %= 10

    nota5 = valor // 5
    valor %= 5

    nota1 = valor

    print('Notas fornecidas:')
    
    if nota100 > 0:
        print(f'{nota100} nota(s) de 100')

    if nota50 > 0:
        print(f'{nota50} notas(s) de 50')

    if nota10 > 0 :
        print(f'{nota10} notas(s) de 10')

    if nota5 > 0 :
        print(f'{nota5} notas(s) de 5')

    if nota1 > 0 :
        print(f'{nota1} nota(s) de 1')