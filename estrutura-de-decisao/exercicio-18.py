# Exercício 18
# Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

try:

    data = input('Digite uma data no formato dd/mm/aaaa: ')

    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    ano_bisssexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)  

    if mes in (1,3,5,7,8,10,12):
        ultimo_dia = 31
    elif mes in (4,6,9,11):
        ultimo_dia = 30
    elif mes == 2:
        if ano_bisssexto:
            ultimo_dia = 29
        else:
            ultimo_dia = 28
    else:
        ultimo_dia = 0

    if 1 <= mes <= 12 and 1 <= dia <= ultimo_dia:
        print('Data válida!')

    else:
        print('Data inválida!')

except ValueError:
    print('Comando inválido')