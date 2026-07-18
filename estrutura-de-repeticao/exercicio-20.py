# Exercício 20
# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True:

    while True:
        numero = int(input('Digite um número inteiro entre 0 e 15: '))

        if 0 <= numero < 16:
            break

        print('Número inválido! Digite um valor entre 0 e 15.')

    fatorial = 1

    for i in range(numero, 0, -1):
        fatorial *= i

    print(f'O fatorial de {numero} é {fatorial}.')

    resposta =input('Deseja calcular outro fatorial? (S/N): ').strip().upper()
    
    if resposta != 'S':
        print('Programa encerrado...')
        break