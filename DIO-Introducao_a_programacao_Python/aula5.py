lista = [3, 1, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'arara']

print(sum(lista)) #Soma todos os elementos da array. Eles devem ser do mesmo tipo, inteiro, no caso.
print(max(lista)) #exibe o maior valor da lista, não importanto a localização.
print(min(lista)) #exibe o menor valor da lista, não importanto a localização.
print(max(lista_animal)) #exibe o maior valor da lista. Com strings, segue a ordem alfabética.
print(min(lista_animal)) #exibe o maior valor da lista. Com strings, segue a ordem alfabética.

nova_lista = lista_animal * 3 #Multiplica os valores dentro da lista.
print(nova_lista)

if 'lobo' in lista_animal: #Procura um valor na lista.
    print('Existe este animal na lista')
else:
    print('Não existe este animal na lista. Será incluido.')
    lista_animal.append('lobo') #Adiciona na lista.
    print(lista_animal)

lista_animal.pop() #Remove o último da lista. Outro exemplo, lista_animal.pop(1), removeria o item da posição 1.
print(lista_animal)

lista_animal.remove('elefante') #Remove um item específico.
print(lista_animal)

#ORDENAÇÃO DAS LISTAS
lista.sort()
lista_animal.sort()
print(lista_animal)
print(lista)
lista.reverse() #Ordenação reversa. Do final para o começo.
lista_animal.reverse()
print(lista_animal)
print(lista)

lista_animal[0] = 'macaco' #Substitui o valor da posição na lista.

#TUPLA - É uma lista que não pode ser alterada. Lista usa [] e Tupla usa ()
tupla = (1, 10, 12, 14)
print(len(tupla)) #Retorna quantos elementos tem na tupla ou na lista.
tupla_animal = tuple(lista_animal) #Converte uma lista em uma tupla.
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla) #Converte uma tupla em uma lista.
print(type(lista_numerica))
print(lista_numerica)