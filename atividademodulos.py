
# CRIE UM MERCADO 

# +
# - UTILIZE LISTAS
# - MOSTRAR O VALOR (módulo separado)**
# - FAZER O PAGAMENTO (módulo separado)
# - FINALIZAR A COMPRA
# - SE DESPEDIR DO USUÁRIO   
# - UTILIZE PARÂMETROS

carrinho = []
valor = []
def mercado():
    print('''
            produtos:

        (0) - arroz > 10,00
        (1) - feijao > 7,00
        (2) - ervilha > 5,00
    ''')

    print('arroz = 10,00, feijao = 7.00 ervilha = 5.00')

    valores = [10.0, 7.0, 5.0]
    produto = ['arroz', 'feijao', 'ervilha']

    
    deseja = input('deseja dar inicio ao pedido? s/n')

    while deseja == 's':
        escolha = int(input('insira o código do produto desejado > '))
        carrinho.append(produto[escolha])
        valor.append(valores[escolha])
        print(carrinho)
        print(valor)
        deseja = input('deseja adicionar mais algum produto ao seu carrinho? s/n ')
    else:
        print(f'seu carrrinho: {carrinho}')


        

def pagamento():
    print('''
        Pagamento

    (1) - pix
    (2) - CD
    (3) - CC
    ''')

    print(carrinho)
    print(valor)
    
    total = sum(valor)
    print(f'O total de tudo ficou: {total}')

    forma = int(input('Escolha sua forma de pagamento com o id correspondente: '))
    
    if forma == 1:
        print('PIX SELECIONADO')
        pagar = input('Digite "s" para pagar> ')
        if pagar == 's':
            print('Compra finalizada')
            print('Obrigado, volte sempre!')
        else:
            print('que pena, tchau!')
    elif forma == 2:
        print('CARTÃO DE DÉBITO SELECIONADO')
        pagar = input('Digite "s" para pagar> ')
        if pagar == 's':
            print('Compra finalizada')
            print('Obrigado, volte sempre!')
        else:
            print('que pena, tchau!')
    elif forma == 3:
        print('CARTÃO CRÉDITO SELECIONADO')
        pagar = input('Digite "s" para pagar> ')
        if pagar == 's':
            print('Compra finalizada')
            print('Obrigado, volte sempre!')
        else:
            print('que pena, tchau!')



mercado()
pagamento()

sair = input('Digite enter para sair do sistema')