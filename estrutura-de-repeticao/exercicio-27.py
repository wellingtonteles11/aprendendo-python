# Exercício 27
# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

quantidade_turmas = int(input('Qual a quantidade de turmas? '))

total_alunos = 0

for i in range(1, quantidade_turmas + 1):
    alunos = int(input(f'Quantos alunos há na turma {i}? '))

    while alunos > 40:
        print('Uma turma não pode ter mais que 40 alunos.')
        alunos = int(input(f'Digite novamnete a quantidade de alunos da turma {i}: '))

    total_alunos += alunos

media = total_alunos / quantidade_turmas
print(f'A média de de alunos por turma é: {media:.2f}')