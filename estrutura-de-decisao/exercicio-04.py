# Exercício 04
# Faça um programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ').lower()

if letra in 'aeiou':
    print(f'A letra "{letra}" é uma vogal.')

elif letra in 'bcdfghjklmnpqrstvwxyz':
    print(f'A letra "{letra}" é uma consoante.')

else:
    print('Comando inválido. Digite uma letra.')