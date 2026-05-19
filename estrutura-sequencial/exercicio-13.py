# Exercício 13
# Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

# Para Megabytes: Gigabytes * 1024
# Para Kilobytes: Gigabytes * 1024 * 1024
# Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.

gigabyte = float(input('Digite o tamanho do arquivo em Gigabytes (GB): '))
conversao_mb = gigabyte * 1024
conversao_kb = gigabyte * 1024 * 1024

print(f'O arquivo tem {conversao_mb:.2f} MBs ou {conversao_kb:.2f} KBs')