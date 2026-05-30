# Exercício 14
# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0         A
# Entre 7.5 e 9.0          B
# Entre 6.0 e 7.5          C
# Entre 4.0 e 6.0          D
# Entre 4.0 e zero         E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

try:
    primeira_nota = float(input('Digite a primeira nota: '))
    segunda_nota = float(input('Digite a segunda nota: '))

    media = (primeira_nota + segunda_nota) / 2

    print(f'Primeira nota: {primeira_nota:.1f}')
    print(f'Segunda nota: {segunda_nota:.1f}')
    print(f'Média: {media:.1f}')

    if 9 <= media <= 10:
        conceito = 'A'
        situacao = 'Aprovado'

    elif 7.5 <= media < 9:
        conceito = 'B'
        situacao = 'Aprovado'

    elif 6 <= media < 7.5:
        conceito = 'C'
        situacao = 'Aprovado'

    elif 4 <= media < 6:
        conceito = 'D'
        situacao = 'Reprovado'

    elif 0<= media < 4:
        conceito = 'E'
        situacao = 'Reprovado'

    else:
        conceito = 'Conceito inválido'
        situacao = 'Situação inválida'

    print(f'Conceito: {conceito}')
    print(f'Situaçao: {situacao}')

except ValueError:
    print('Digite apenas números válidos.')