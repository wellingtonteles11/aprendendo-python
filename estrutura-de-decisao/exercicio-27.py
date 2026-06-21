# Exercício 27
# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                 Até 5 Kg                Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

kg_morango = float(input('Quantos quilos de morango? '))
kg_maca = float(input('Quantos quilos de maçã? '))

if kg_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if kg_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

total_kg = kg_morango + kg_maca
valor_morango = kg_morango * preco_morango
valor_maca = kg_maca * preco_maca
valor_total = valor_morango + valor_maca

if total_kg > 8 or valor_total > 25.00:
    valor_total = valor_total * 0.90

print(f'Valor a ser pago pelo cliente: R$ {valor_total:.2f}')