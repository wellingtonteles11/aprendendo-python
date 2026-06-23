# Exercício 1
# # Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Informe uma nota entre zero e dez: '))

while nota < 0 or nota > 10:
    print('Valor inválido! A nota deve estar entre 0 e 10')
    nota = float(input('Informe uma nota entre zero e dez: '))

print(f'Nota válida registrada: {nota}')
