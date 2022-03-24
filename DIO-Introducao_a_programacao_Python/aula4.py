#MOSTRAR OS NÚMEROS DE 1 a 100 - LAÇO DE REPETIÇÃO
# for x in range(1, 101):
#     print(x)

#ACHAR NÚMEROS PRIMOS
# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1 #div = div + 1
#
# if div == 2:
#     print('Número {} é primo.'.format(a))
# else:
#     print('Número {} não é primo.'.format(a))

#ACHAR NÚMEROS PRIMOS DENTRO DE UM INTERVALO
# for num in range(101):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1 #div = div + 1
#     if div == 2:
#         print(num)

#ACHAR NÚMEROS PRIMOS DENTRO DE UM INTERVALO COM INPUT
# a = int(input('Entre com um valor: '))
# for num in range(a+1): #a+1 para realizar a operação com ele mesmo.
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1 #div = div + 1
#     if div == 2:
#         print(num)

#WHILE - REPETIÇÃO ATÉ QUE UMA CONDIÇÃO OCORRA
# nota = int(input('Entre com a nota: '))
# while nota > 10
#     nota = int(input('Nota inválida. Entre com a nota correta: '))
# a = 0
# while a <= 10:
#     print(a)
#     a += 1

a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Digite novamente o Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Digite novamente o Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Digite novamente o Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Digite novamente o Quarto Bimestre: '))
media = (a + b + c + d) / 4
print('Média: {}'.format(media))