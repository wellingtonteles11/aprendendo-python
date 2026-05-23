# Exercício 10
# Faça um programa que pergunte em que turno você estuda. Peça para digitar:

# M - Matutino
# V - Vespertino
# N - Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Digite "M" para Matutino, "V" para Vespertino e "N" para Noturno: ').lower()

if turno == 'm':
    print('Bom Dia!')

elif turno == 'v':
    print('Boa Tarde!')

elif turno == 'n':
    print('Boa Noite!')

else:
    print('Comando Inválido!')