# Exercício 15
# Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

# Dicas:

# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = int(input('Informe o valor primeiro lado: '))
lado2 = int(input('Informe o valor do segundo lado: '))
lado3 = int(input('Informe o valor do terceiro lado: '))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print('Os valores infomardo formam o triângulo')

    if lado1 == lado2 == lado3:
        print('Classificação: Triângulo Equilatero (três lados iguais)')
    elif (lado1 == lado2) or (lado1 == lado3) or (lado3 == lado2):
        print('Classificação: Triângulo Isóceles (dois lados iguais)')
    else:
        print('Classificação: Triângulo Escaleno (todos os lados diferentes)')

else:
    print('Os valores informados não podem formar um triângulo')