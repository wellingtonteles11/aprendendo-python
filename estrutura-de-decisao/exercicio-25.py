# Exercício 25
# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

contador = 0

perguntas = [
    'Telefonou para a vítima ?',
    'Esteve no local do crime ?',
    'Mora perto da vítima ?',
    'Devia para vítima ?',
    'Já trabalhou com a vítima?'
]

for pergunta in perguntas:
    while True:
        resposta = input(f'{pergunta} (S/N): ').lower()

        if resposta == 's':
            contador += 1
            break

        elif resposta == 'n':
            break
        else:
             print('Comando inválido!')

if contador == 2:
    print('Suspeito')

elif 3 <= contador <= 4:
    print('Cúmplice')

elif contador == 5:
    print('Assassino')

else:
    print('Inocente')

