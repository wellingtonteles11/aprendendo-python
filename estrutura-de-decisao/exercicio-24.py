# Exercício 24
# Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

# par ou ímpar;
# positivo ou negativo;
# inteiro ou decim  

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

operacao = input('Digite a operaçao (+, -, *, /): ')
try:
    if operacao == '+':
        resultado = primeiro_numero + segundo_numero
    elif operacao == '-':
        resultado = primeiro_numero - segundo_numero
    elif operacao == '*':
        resultado = primeiro_numero * segundo_numero
    elif operacao == '/':
        resultado = primeiro_numero / segundo_numero
    
    else: 
        print('Operação inválida.')
        exit()
except ZeroDivisionError:
    print('Não é possível dividir por zero') 
    exit()

print(f'O resultado da operação é: {resultado}')

if resultado % 1 == 0:
    if resultado % 2 == 0:
        print('O resultado é: Par')
    else:
        print('O resultado é: Impar')

if resultado > 0:
    print('Resultado é: Positivo')
elif resultado < 0:
    print('Resultado é: Negativo')
else:
    print('Resultado é: Zero (neutro)')

if resultado % 1 == 0:
    print('O resultado é inteiro')

else:
    print('O resultado é décimal')







