print('Bem-vindo a loja do Eduardo de Castro Santos')
valor_pedido = float(input('Entre com o valor do pedido: '))
quantidade_parcelas = int(input('Entre com a quantidades de parcelas : '))

# Calculando o juros (j)

j = valor_pedido*(1+0/100)/quantidade_parcelas
j1 = valor_pedido*(1+4/100)/quantidade_parcelas
j2 = valor_pedido*(1+8/100)/quantidade_parcelas
j3 = valor_pedido*(1+16/100)/quantidade_parcelas
j4 = valor_pedido*(1+32/100)/quantidade_parcelas

# Usando o if,elif e else + print

if quantidade_parcelas <4:
    print(f'valor da parcela :R${(round(j, 2))}   \nvalor total parcelado :R${(round(j*quantidade_parcelas, 2))}')
elif 4 <= quantidade_parcelas <6 :
    print(f'valor da parcela :R${(round(j1, 2))}   \nvalor total parcelado :R${(round(j1*quantidade_parcelas, 2))}')
elif 6 <= quantidade_parcelas <9 :
    print(f'valor da parcela :R${(round(j2, 2))}   \nvalor total parcelado :R${(round(j2*quantidade_parcelas, 2))}')
elif 9 <= quantidade_parcelas <13 :
    print(f'valor da parcela :R${(round(j3, 2))}   \nvalor total parcelado :R${(round(j3*quantidade_parcelas, 2))}')
else:
    print(f'valor da parcela :R${(round(j4, 2))}   \nvalor total parcelado :R${(round(j4*quantidade_parcelas, 2))}')
