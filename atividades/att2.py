print('-----Bem vindos a loja de marmitas do Eduardo de Castro Santos-----')
# Criando o menu
print('-----------------------------Cardápio------------------------------')
print('-----| Tamanho  | Bife acebolado(BA)  | Filé de frango(FF)  |------')
print('-----|    P     |      R$ 16.00       |      R$ 15.00       |------')
print('-----|    M     |      R$ 18.00       |      R$ 17.00       |------')
print('-----|    G     |      R$ 22.00       |      R$ 21.00       |------')
print('-------------------------------------------------------------------')
# Colocando os preços para calcular o valor total

precos ={('BA', 'P'): 16,
         ('BA', 'M'): 18,
         ('BA', 'G'): 22,
         ('FF', 'P'): 15,
         ('FF', 'M'): 17,
         ('FF', 'G'): 21,}

total_acumulado = 0
# usando o while, continue e break

while True:
    sabor = input('\nEntre com o sabor desejado (BA/FF): ').upper()
    tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()

    if (sabor, tamanho) in precos:
        valor_pedido = precos[(sabor, tamanho)]
        total_acumulado += valor_pedido
        print(f'Você escolheu um {sabor} no tamanho {tamanho}: R$ {valor_pedido}')
    else:
        print('Escolha inválida, Por Favor tente novamente.')
        continue
    deseja_continuar = input('\nDeseja mais alguma coisa? (S/N): ').upper()
    if deseja_continuar == 'N':
        print(f'O valor total a ser pago é: R$ {total_acumulado}')
        break
