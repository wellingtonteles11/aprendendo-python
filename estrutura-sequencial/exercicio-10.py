# Exercício 10
# Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

graus_celsius = float(input('Informe a temperatura em Celsius: '))
graus_fahrenheit = (graus_celsius * 9 / 5) + 32
print(f'A conversão de {graus_celsius:.2f}C para Fahrenheit é: {graus_fahrenheit:.2f}F ')