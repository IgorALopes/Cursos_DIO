#CONJUNTOS se caracterizam por {}

# conjunto = {1, 2, 3, 4, 4, 2} #CONJUNTOS não apresentam duplicidades
# print(type(conjunto))
# print(conjunto)
# conjunto.add(5) #Adiciona um elemento
# conjunto.discard(2) #Remove um elemento
# print(conjunto)

#União entre conjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
#Intersecção entre conjuntos. Pega apenas os elementos em comuns.
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
#Diferença. Recebe apenas os elementos que não existem no outro conjunto
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre conjuntos 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre conjuntos 2 e 1: {}'.format(conjunto_diferenca2))
#Diferença simétrica. Recebe tudo que só tem em um e no outro.
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença Simétrica: {}'.format(conjunto_diff_simetrica))
#Subconjunto. Saber se os elementos de um conjunto se apresentam dentro de outro.
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B? {}'.format(conjunto_subset))
#Superconjunto. O contrário de subconjunto.
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A? {}'.format(conjunto_superset))

#Retirar duplicidade de listas. Basta converter para conjunto e depois lista de novo.
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista) #Conversão para lista.
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)