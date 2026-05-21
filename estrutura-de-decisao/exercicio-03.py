# Exercício 03
# Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

# F - Feminino
# M - Masculino
# Sexo Inválido.

letra = input('Digite a letra "M" para Masculino e "F" para Feminino: ').lower()

if letra == 'm':
    print('O sexo é masculino')

elif letra == 'f':
    print('O sexo é feminino')

else:
    print('Sexo inválido')
    