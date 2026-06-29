# Exercício 2
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')

    if usuario == senha:
        print('Erro! A senha não pode ser igual ao nome de usuário.')
        continue

    maiuscula = 0
    minuscula = 0
    numeros = 0
    especiais = 0

    for caractere in senha:
        if caractere.isupper():
            maiuscula += 1
        elif caractere.islower():
            minuscula += 1
        elif caractere.isdigit():
            numeros += 1
        else:
            especiais += 1

    if len(senha) < 8:
        print('A senha deve ter no mínimo 8 caracteres.')
    elif maiuscula < 2:
        print('A senha deve ter pelo menos 2 letras maiúculas.')
    elif minuscula < 2:
        print('A sneha deve ter pelo menos 2 letras minúsculas.')
    elif numeros < 2:
        print('A senha deve ter pelo menos 2 múmeros.')
    elif especiais < 2:
        print('A senha deve ter pelo menos 2 caractares especiais')

    else:
        print('Cadastro realizado com sucesso!')
        break
