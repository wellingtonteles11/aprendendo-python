# Exercício 17
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input('Digite um número inteiro: '))

fatorial = 1

for i in range(numero, 0, -1):
    fatorial *= i

print(f'O fatorial de {numero} é {fatorial}.')