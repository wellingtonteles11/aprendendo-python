# Exercício 3
# Faça um programa que leia e valide as seguintes informações:

# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input('Digite seu nome: ')
    if len(nome) > 3:
        break
    else:
        print('O nome deve conter mais de 3 caracteres.')

while True:
    idade = int(input('Digite a sua idade: '))
    if 0 <= idade <= 150:
        break
    else:
        print('A idade deve estar entre 0 a 150.')

while True:
    salario = float(input('Digite seu salário: '))
    if salario > 0:
        break
    else:
        print('O salário deve ser maior que zero.')

while True:
    estado_civil = input('Digite seu estado civil (s/c/v/d): ').lower()
    if estado_civil in ('s', 'c', 'v', 'd'):
        break
    else:
        print('Estado civil inválido')

print('Dados cadastrados com sucesso!')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: R$ {salario:.2f}')
print(f'Estado civil: {estado_civil}')

