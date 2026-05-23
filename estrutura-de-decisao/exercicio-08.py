# Exercício 08
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:

produto_teclado = float(input('Informe o valor da teclado: '))
produto_fone = float(input('Informe o valor do fone: '))
produto_mouse = float(input('Informe o valor do mouse:'))

if produto_teclado == produto_fone == produto_mouse:
    print('Todos os produtos possuem o mesmo valor')

elif produto_teclado <= produto_fone and produto_teclado <= produto_mouse:
    print(f'O teclado é mais barato. Custa somente R$ {produto_teclado:.2f}')

elif produto_fone <= produto_teclado and produto_fone <= produto_mouse:
    print(f'O fone é mais barato. Custa somente R$ {produto_fone:.2f}')

else:
    print(f'O mouse é mais barato. Custa somente R$ {produto_mouse:.2f}')
