estoque = []

while True:
    menu = int(input('''
    ------- Menu ------
    [1] Cadastrar Produto
    [2] Atualizar Produto             
    [3] Remover Produto
    [4] Exibir Produto
    [5] Realizar Venda                 
    [6] Sair                                                
    Opção: '''))

#condição
    if menu == 1:
        produto = dict(
            nome = str(input('\nNome do produto:')).title(),
            quantidade = int(input('Quantidade em estoque:')),
            preco = float(input('Preço unitário:'))
        )

        estoque.append(produto)
        print('\nProduto cadastrado com sucesso.\n')
       
    elif menu == 2:
        nome = str(input('\nNome do produto:')).title()
        for produto in estoque:
            if produto['nome'] == nome:
                produto['quantidade'] = int(input('Nova quantidade:'))
                produto['preco'] = float(input('Novo preço:'))
                print('\nProduto atualizado com sucesso.\n')
                break
        else:
            print('\nProduto não encontrado.\n')

    elif menu == 3:
        nome = str(input('\nNome do produto:')).title()
        for produto in estoque:
            if produto['nome'] == nome:
                estoque.remove(produto)
                print('\nProduto removido com sucesso.')
                break
        else:
            print(f'\nPrdouto não encontrado.\n')

    elif menu == 4:
        print('\nEstoque de produtos:\n')
        for produto in estoque:
            print('Nome: ', produto['nome'])
            print('Quantidade: ', produto['quantidade'])
            print('Preço: ', produto['preco'])
            print('----------------------------')

    elif menu == 5:
        total_geral_vendas=0
        while True:
            nome = str(input('\nNome do produto vendido:')).title()
            if  nome == 'Fechar':
                print(f'\nTotal geral das vendas: R${round(total_geral_vendas, 2)}\n')
                print('Venda finalizada.\n')
                break
            qtd_vendida = int(input('Quantidade vendida:'))
            produto_encontrado = False
            for produto in estoque:
                if produto['nome'] == nome:
                    produto_encontrado = True
                    if qtd_vendida <= produto['quantidade']:
                        produto['quantidade'] -= qtd_vendida
                        total_venda = qtd_vendida * produto['preco']
                        total_geral_vendas += total_venda
                        print(f'Total da venda deste produto: R${round(total_venda, 2)}')
                        print(f'\nTotal geral acumulado: R${round(total_geral_vendas, 2)}\n')
                        break
                    else:
                        print('\nQuantidade insuficiente em estoque.\n')
                        break
            if not produto_encontrado:
                print('\nProduto não encontrado.\n')
            else:
                print('Digite "Fechar" para encerrar a venda ou continue adicionando produtos.')

    elif menu == 6:
        print('\nSaindo do sistema.\n')
        break
    else:
        print('\nOpção inválida!\n')