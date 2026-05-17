# Exercício 04
# Faça um programa que peça as 4 notas bimestrais e mostre a média.

primera_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))
quarta_nota = float(input('Digite a quarta nota: '))

media = (primera_nota + segunda_nota + terceira_nota + quarta_nota) / 4
print(f'A média das notas do aluno é: {media:.1f}')