# Exercício 5
# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

while True:

    while True:
        populacao_a = int(input('Digite a população do país A: '))
        if populacao_a > 0:
            break
        print('A população deve ser maior que zero.')

    while True:
        populacao_b = int(input('Digite apopulação do do país B: '))
        if populacao_b > 0:
            break
        print('A população deve ser maior que zero.')

    while True:
        taxa_a = float(input('Digite a taxa de crescimento do país A (%): '))
        if taxa_a > 0:
            taxa_a = taxa_a / 100
            break
        print('A taxa deve ser maior que zero.')

    while True:
        taxa_b = float(input('Digite a taxa de crescimento do país B (%): '))
        if taxa_b > 0:
            taxa_b = taxa_b / 100
            break
        print('A taxa deve ser maior que zero.')

    anos = 0

    while populacao_a < populacao_b:
        populacao_a += populacao_a * taxa_a
        populacao_b += populacao_b * taxa_b
        anos += 1

    print(f'Número de anos: {anos}')
    print(f'População do País A: {int(populacao_a)} habitantes')
    print(f'População do País B: {int(populacao_b)} habitantes')
    
    repetir = input('Deseja realizar outro cálculo? (s/n): ').lower()
    if repetir != 's':
        print('Programa encerrado.')
        break