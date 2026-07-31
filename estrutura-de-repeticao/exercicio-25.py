# Exercício 25
# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

quantidade_pessoas = int(input('Quantas pessoas há na turma? '))

soma_idade = 0

for i in range(1, quantidade_pessoas + 1):
    idade = int(input(f'Digite a idade de {i}ª pessoa: '))
    soma_idade += idade

media = soma_idade / quantidade_pessoas

print(f'Média de idade: {media:.2f}')

if media <= 25:
    print('A turma é jovem.')

elif media <= 60:
    print('A turma é adulta.')

else:
    print('A turma é idosa.')