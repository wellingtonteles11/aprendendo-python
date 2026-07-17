# Exercício 15
# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input('Digite a quantidade de termo da sequência de Fibonacci: '))

primeiro = 1
segundo = 1

if n <= 0:
    print('Digite um número maior que zero.')
elif n == 1:
    print(primeiro)
else:
    print(primeiro)
    print(segundo)

    for i in range(3, n + 1):
        proximo = primeiro + segundo
        print(proximo)
        primeiro = segundo
        segundo = proximo