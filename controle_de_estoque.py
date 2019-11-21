def mainfuncionario():



    print('1 - Para listar todos os itens do estoque')
    print('2 - Para adicionar item no estoque')
    print('3 - Para remover itens do estoque')
    print('0 - Para fechar o programa')

    opcao = int(input('Entre com a opcao desejada'))

    while opcao > 0:
    
        if opcao < 0 or opcao > 3:
            print('Entre APENAS com alguma das opcoes listadas')
            main()

        elif(opcao == 1):
            listar_estoque(lista)

        elif(opcao == 2):
            adiocinar_item_estoque(estoque)

        elif(opcao == 3):
            remover_item_estoque(estoque)




defmainadm():


    print('1 - Para listar todas as alterações feitas pelos funcionários')
    print('2 - Para adicionar cadastro de funcionário')
    print('3 - Remover cadastro de funcionário')
    print('4 - Para listar o estoque total antes das alterações')
    print('5 - Para adicionar item no estoque')
    print('6 - Para remover item do estoque')
    print('7 - Para zerar o estoque')
    print('8 - Para criar um estoque')
    print('0 - Para fechar o programa')

    opcao = int(input('Entre com a opcao desejada'))

    while opcao > 0:

        if opcao < 0 or opcao > 3:
            print('Entre APENAS com alguma das opcoes listadas')
            main()

        elif(opcao == 1):
            listar_alteracoes_estoque(estoque)
            print(listar_alteracoes_estoque(estoque)

        elif(opcao == 2):
            adicionar_cadastro_funcionario()

        elif(opcao ==  3):
            demissao()

        elif(opcao == 4):
            listar_estoque_total()

        elif(opcao == 5):
            adicionar_item_estoque(estoque)

        elif(opcao == 6):
            remover_item_estoque(estoque)

        elif(opcao == 7):
            zerar_estoque(estoque)

        elif(opcao == 8):
            criar_estoque()

        












                  

def login

        
