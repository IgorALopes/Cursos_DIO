#SABER QUAL O MAIOR NÚMERO
print('Início programa1 - SABER QUAL O MAIOR NÚMERO.')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O maior número é {}'.format(a))
elif b > a and b > c: #elif = else if
    print('O maior número é {}'.format(b))
else:
    print('O maior número é {}'.format(c))
print('Final do programa1.')

#SABER SE O NÚMERO É PAR
print('Início programa2 - SABER SE O NÚMERO É PAR.')
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = b % 2
if resto_a == 0 or resto_b == 0: #pode-se utilizar o 'or not' para inverter a condição booleana seguinte e transforma-la em 'false' neste caso, e desenvolver do outra forma.
    print('Foi digitado um número par.')
else:
    print('Nenhum número par foi digitado.')
print('Final do programa2.')

#MÉDIA COM VALIDAÇÃO
print('Início programa3 - MÉDIA COM VALIDAÇÃO.')
#Validação a cada campo preenchido.
a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Digite novamente o Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Digite novamente o Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Digite novamente o Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Digite novamente o Quarto Bimestre: '))
media = (a + b + c + d) / 4
print('Média: {}'.format(media))

#Validação após todos os campos preenchidos.
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada.')

print('Final do programa3.')