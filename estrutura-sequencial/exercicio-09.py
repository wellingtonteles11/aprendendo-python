# Exercício 09
# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

graus_fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))
graus_celsius = 5 * ((graus_fahrenheit - 32) / 9)
print(f'A conversão de {graus_fahrenheit:.1f}F para Celsius é: {graus_celsius:.1f}C')