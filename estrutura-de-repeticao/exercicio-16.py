# Exercício 16
# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

primeiro_numero = 0
segundo_numero = 1

print(primeiro_numero)
print(segundo_numero)

while True:
    proximo = primeiro_numero + segundo_numero

    if proximo > 500:
        break

    print(proximo)

    primeiro_numero = segundo_numero
    segundo_numero = proximo