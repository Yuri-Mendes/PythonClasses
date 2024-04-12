usuarios=[]
#loop menu principal
while True:
    print('\nMenu')
    print('1 - Inserir novo usuário')
    print('2 - Exibir dados dos usuários.')
    print('3 - Exibir o IMC dos usuários.')
    print('4 - Deletar usuário.')
    print('5 - Sair.')
    opcao=input(('\nEscolha uma opção:'))
#condição
    if opcao == '1':
        nome=str(input('Digite o nome do usuário: ')).capitalize()
        idade=int(input('Digite a idade: '))
        peso=float(input('Digite o peso: '))
        altura=float(input('Digite a altura: '))
        usuarios.append((nome,idade,peso,altura))
        print('\nUsuários adicionados com sucesso!\n')

    elif opcao == '2':
        if usuarios:
            print('\nDados dos usuários')
            for usuario in usuarios:
                nome,idade,peso,altura = usuario
                print(f'Nome: {nome}, Idade: {idade}, Peso: {peso}, Altura: {altura}')
        else:
            print('\nNão há usuários cadastrados.\n')

    elif opcao == '3':
        if usuarios:
            print('\nIMC dos usuários')
        for usuario in usuarios:
            nome,idade,peso,altura = usuario
            imc = peso / (altura**2)
            print(f'O IMC do usuário {nome} é: {imc:.2f}')
            if imc<18.5:
                resultado = 'Abaixo do peso.'
            elif 18.5 <=  imc < 24.9:
                resultado = 'Peso Normal.'
            elif 24.9 <=  imc < 29.9:
                resultado = 'Sobrepeso.'
            elif 29.9 <=  imc < 34.9:
                resultado = 'Obesidade classe I.'
            elif 34.9 <=  imc < 39.9:
                resultado = 'Obesidade classe II.'
            elif imc > 40:
                resultado = 'Obesidade classe III.'
        else:
            print(f'\nEste é o IMC do usuário: {resultado}\n')

    elif opcao == '4':
        if usuarios:
            remover_user=str(input("\nDigite o nome do usuário que deseja remover: ")).title()
        for usuario in usuarios:
            if usuario [0] == nome:
                usuarios.remove(usuario)
                print(f'\nUsuário {remover_user} removido com sucesso.\n')
                break
        else:
            print('\nUsuário não encontrado.\n')

    elif opcao == '5':
        print('\nSaindo do sistema\n')
        break
    else:
        print('\nOpção inválida!\n')
            
    