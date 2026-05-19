# Exercício 12
# Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:

gigabyte = float(input('Digite o tamanho do arquivo em Gigabytes (GB): '))
conversao_mb = gigabyte * 1024
print(f'A conversão de {gigabyte} GB equivalem a {conversao_mb:.2f} Megabytes (MB)')