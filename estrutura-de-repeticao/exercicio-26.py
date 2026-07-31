# Exercício 26
# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

total_eleitores = int(input('Digite o número de eleitores: '))

candidato1 = 0
candidato2 = 0
candidato3 = 0

for i in range(1, total_eleitores + 1):
    voto = int(input(f'Eleitor {i}, vote (1, 2, ou 3): '))
   
    if voto == 1:
         candidato1 += 1
    elif voto == 2:
         candidato2 += 1
    elif voto == 3:
         candidato3 += 1
    else:
        print('Candidatado inválido!')
        


print(f'Canditado 1: {candidato1} votos.')
print(f'Candidato 2: {candidato2} votos.')
print(f'Candidato 3: {candidato3} votos')

