# Exercício 19
# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

quantidade = int(input('Quantos números você deseja digitar? '))

maior = None
menor = None
soma = 0

for i in range(quantidade):
    while True:
        numero = int(input(f'Digite o {i + 1}º número (0 a 1000): '))

        if 0 <= numero <= 1000:
            break

        print('Número inválido! Digite um valor entre 0 e 100.')

    soma += numero

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
print(f'Soma dos números: {soma}')