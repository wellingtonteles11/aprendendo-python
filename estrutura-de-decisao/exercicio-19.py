# Exercício 19
# Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

# 326 = 3 centenas, 2 dezenas e 6 unidades

# 12 = 1 dezena e 2 unidades

# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = int(input('Digite um número menor que 1000: '))

if numero < 0 or numero >= 1000:
    print('Número inválido')

else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    if centenas > 0:
        if centenas == 1:
            partes.append('1 centena') 
        else:
            partes.append(f'{centenas} centenas')

    if dezenas > 0:
        if dezenas == 1:
            partes.append('1 dezena') 
        else:
            partes.append(f'{dezenas} dezenas')

    if unidades > 0:
        if unidades == 1:
            partes.append('1 unidade')
        else:
            partes.append(f'{unidades} unidades')
    
    if len(partes) == 0:
        resultado = '0 unidades'
    elif len(partes) == 1:
        resultado = partes[0]
    elif len(partes) == 2:
        resultado = ' e '.join(partes)
    else:
        resultado = f'{partes[0]}, {partes[1]} e {partes[2]}'

    print(f'{numero} = {resultado}')


