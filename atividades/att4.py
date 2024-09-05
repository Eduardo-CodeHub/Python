print('Bem Vindos a Empresa do Eduardo de Castro Santos')


lista_funcionarios = []
id_global = 5702024

# Função para cadastrar um funcionário
def cadastrar_funcionario(id):
    print('-' * 46)
    print('----------MENU CADASTRAR FUNCIONÁRIO----------')
    id = print(f'id do Funcionário: {id_global}')
    nome = input('Por favor entre com o nome do Funcionário: ')
    setor = input('Por favor entre com o setor do Funcionário: ')
    salario = float(input('Por favor entre com o salário do Funcionário: '))

    funcionario = {
        'id': id_global,
        'nome': nome,
        'setor': setor,
        'salario': salario}

    lista_funcionarios.append(funcionario.copy())

# Função para consultar funcionários
def consultar_funcionarios():
    while True:
        print('-' * 46)
        print('----------MENU CONSULTAR FUNCIONÁRIO----------')
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos os Funcionários')
        print('2 - Consultar Funcionário por id')
        print('3 - Consultar Funcionário(s) por setor')
        print('4 - Retornar')

        opcao = int(input('>> '))

        if opcao == 1:
            for funcionario in lista_funcionarios:
                print(funcionario)
        elif opcao == 2:
            id_consulta = int(input('Digite o ID do funcionário: '))
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print(funcionario)
                    break
            else:
                print('ID inválido.')
        elif opcao == 3:
            setor_consulta = input('Digite o setor: ')
            for funcionario in lista_funcionarios:
                if funcionario['setor'] == setor_consulta:
                    print(funcionario)
        elif opcao == 4:
            break
        else:
            print('Opção inválida.')

# Função para remover funcionário
def remover_funcionario():
    id_remocao = int(input('Digite o ID do funcionário a ser removido: '))
    for funcionario in lista_funcionarios:
        if funcionario['id'] == id_remocao:
            lista_funcionarios.remove(funcionario)
            print('Funcionário removido com sucesso!')
            break
    else:
        print('ID inválido.')

# Menu principal
while True:
    print('-' * 40)
    print('-------------MENU PRINCIPAL-------------')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Funcionários')
    print('2 - Consultar Funcionário(s)')
    print('3 - Remover Funcionário')
    print('4 - Sair')

    opcao_menu = int(input('>> '))

    if opcao_menu == 1:
        id_global += 1
        cadastrar_funcionario(id_global)
    elif opcao_menu == 2:
        consultar_funcionarios()
    elif opcao_menu == 3:
        remover_funcionario()
    elif opcao_menu == 4:
        print('Encerrando o programa. Obrigado!')
        break
    else:
        print('Opção inválida.')
