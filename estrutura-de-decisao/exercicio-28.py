# Exercício 28
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                 Até 5 Kg                Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print('==== HIPERMERCADO TABAJARA ====')

print('1 - Filé duplo')
print('2 - Alcatra')
print('3 - Picanha')

tipo_carne = input('Escolha o tipo de carne: ')

while tipo_carne not in ['1', '2', '3']:
    print('Tipo de carne inválido!')
    tipo_carne = input('Escolha o tipo de carne: ')
   
quantidade_kg = float(input('Quantidade (kg): '))

if tipo_carne == '1':
    carne = 'Filé duplo'
    preco_kg = 4.90 if quantidade_kg <= 5 else 5.80

elif tipo_carne == '2':
    carne = 'Alcatra'
    preco_kg = 5.90 if quantidade_kg <= 5 else 6.80

elif tipo_carne == '3':
    carne = 'Picanha'
    preco_kg = 6.90 if quantidade_kg <= 5 else 7.80

total = quantidade_kg * preco_kg

cartao = input('Pagamento com cartão Tabajara? (S/N): ').upper()

if cartao == 'S':
    desconto = total * 0.05
    pagamento = 'Cartão Tabajara'

else:
    desconto = 0
    pagamento = 'Outro'

valor_final = total - desconto

print('==== CUPOM FISCAL ====')
print(f'Tipo de carne: {carne}')
print(f'Quantidade: {quantidade_kg:.2f}')
print(f'Preço total: R$ {total:.2f}')
print(f'Tipo de pagamento: {pagamento}')
print(f'Valor de desconto: R$ {desconto:.2f}')
print(f'Valor a pagar: R$ {valor_final:.2f}')





