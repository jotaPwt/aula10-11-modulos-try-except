# tratamento de excessoões

# try:
#     div = 10/0
#     print(div)
# except:
#     print('erro')



# try:
#     n = float(input('digite um numero real'))
#     print(n)
# except:
#     print(erro)
# else:
#     print('else')
# finally:
#     print('carregamento finalizado')


# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

try:
    num = int(input('Digite um numero: '))
except ValueError as error:
    print(error)

# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

try:
    n1 = int(input('> '))
    n2 = int(input('> '))
    div = n1 / n2
    print(div)
except ZeroDivisionError as erro:
    print(erro)

# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e retorne o elemento naquele índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

lista = [0,1,2]
def verifica(lista):
    try:
        n = int(input('>> '))
        i = lista[n]
        print(i)
    except:
        print('esse indice não existe')    

verifica(lista)

# Exercício 4:
# Crie uma função que divida dois números e manipule a exceção caso o divisor seja zero.

# def manipule():
#     try:
#         n1 = int(input('> '))
#         n2 = int(input('> '))
#         div = n1 / n2
#         print(div)
#     except ZeroDivisionError as erro:
#         print(erro)
