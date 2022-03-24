
lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[1]
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre Executa')
    print('Fechando o arquivo')
    arquivo.close()