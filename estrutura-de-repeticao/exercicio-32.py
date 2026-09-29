# Exercício 32
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

# Fatorial de: 5 5! = 5 . 4 . 3 . 2 . 1 = 120

numero = int(input('Fatorial de: '))

fatorial = 1
contador = numero

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f'{numero}! = ', end='')

contador = numero

while contador > 0:
    print(contador, end='')
    
    if contador > 1:
        print('.', end='')

    contador -= 1

print(f'= {fatorial}')

