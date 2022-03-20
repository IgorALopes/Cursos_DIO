a = int(input('Entre com o primeiro valor: ')) #Já transforma o input do usuário (que seria uma string) em inteiro, para a realização das operações aritméticas.
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('soma: ' + str(soma)) #transformei a variável soma em string pois não é possível concatenar varieveis inteiros com strings.
print(subtracao)
print(multiplicacao)
print(type(divisao)) #a variável divisão é do tipo float.
print(int(divisao)) #tranforma divisao em inteiro para não aparecer as casas decimais.
print(resto)

# FORMA MAIS USADA PARA CONCATENÇÃO.
print('Soma: {som}. ' 
      '\nSubtração: {sub}. '
      '\nMultiplicação: {mult}. '
      '\nDivisão: {div}. '
      '\nResto: {rest}. '.format(som=soma,
                                 sub=subtracao,
                                 mult=multiplicacao,
                                 div=divisao,
                                 rest=resto)) #cria alias dentro da string do print utilizando {} e depois indica com o format quem são.

x = '1' #string
soma2 = int(x) + 1 #transforma x em inteiro para poder realizar a soma
print(soma2)
