# Exercício 22
# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

numero = int(input('Digite um número inteiro: '))

if numero <= 1:
    print('Não é um número primo.')
else:
    primo = True

    for i in range(2,numero):
        if numero % i == 0:
            if primo:
                print(f'{numero} não é um número primo')
                print('É divisivel por:')
                primo = False

            print(i)

    if primo:
        print(f'{numero} é um número primo.')