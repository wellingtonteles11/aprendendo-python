# Exercício 11
# Altere o programa anterior para mostrar no final a soma dos números.

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

soma = 0

if primeiro_numero <= segundo_numero:
    for i in range(primeiro_numero, segundo_numero + 1):
        print(i)
        soma += i

else:
    for i in range(segundo_numero, primeiro_numero + 1):
        print(i)
        soma += 1

print(f'A soma do número é: {soma}')