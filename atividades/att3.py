print('Bem-vindos a Fábrica de Camisetas do Eduardo de Castro Santos')

# fazendo o "menu" e colocando o valor unitário de cada camisa
def escolha_modelo():

    while True:
        modelo = input('\nEntre com o modelo desejado'
                       '\nMCS - Manga Curta Simples'
                       '\nMLS - Manga Longa Simples'
                       '\nMCE - Manga Curta Com Estampa'
                       '\nMLE - Manga Longa Com Estampa'
                       '\n>> ').upper()
        if modelo in ['MCS', 'MLS', 'MCE', 'MLE']:
            break
        else:
            print('\nEscolha inválida, Entre com o modelo novamente')


    valores = {'MCS': 1.80, 'MLS': 2.10, 'MCE': 2.90, 'MLE': 3.20}
    return valores[modelo]


def num_camisetas():

    while True:
        try:
            num_camisetas = int(input('Digite o número de camisetas: '))
            if num_camisetas > 20000:
                print('Não aceitamos tantas camisetas de uma vez.'
                      '\nPor favor, Entre com o numero de camisetas novamente')
            else:
                break
        except ValueError:
            ''

    # Cálculo do desconto
    if num_camisetas < 20:
        desconto = 0
    elif 20 <= num_camisetas < 200:
        desconto = 0.05
    elif 200 <= num_camisetas < 2000:
        desconto = 0.07
    elif 2000 <= num_camisetas <= 20000:
        desconto = 0.12

    return num_camisetas * (1 - desconto)

# Função do frete
def frete():

    while True:
        try:
            opcao_frete = int(input('\nEscolha o tipo de frete: '
                                    '\n1 - Frete por transportadora - R$ 100.00 '
                                    '\n2 - Frete por Sedex - R$ 200.00 '
                                    '\n0 - Retirar Pedido na fábrica - R$ 0.00'
                                    '\n>> '))
            if opcao_frete in [0, 1, 2]:
                break
            else:
                print('Opção inválida. Escolha entre 1, 2 ou 0.')
        except ValueError:
            print('Por favor, digite um valor numérico válido.')

    # Valores dos fretes
    valores_frete = {1: 100, 2: 200, 0: 0}
    return valores_frete[opcao_frete]


# Função (main)
if __name__ == '__main__':

 valor_modelo = escolha_modelo()
 num_camisetas_desconto = num_camisetas()
 valor_frete = frete()

# Cálculo do total a pagar
total = (valor_modelo * num_camisetas_desconto) + valor_frete
print(f'\nTotal: R$ {total:.2f}')