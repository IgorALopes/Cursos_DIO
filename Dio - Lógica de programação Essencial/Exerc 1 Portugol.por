programa
{
	
	funcao inicio()
	{
		real janeiro,fevereiro,marco,abril,media,total
		cadeia nome

		escreva("Escreva o seu nome: ")
		leia(nome)
		escreva("Seu total de vendas em janeiro: R$")
		leia(janeiro)
		escreva("Seu total de vendas em fevereiro: R$")
		leia(fevereiro)
		escreva("Seu total de vendas em março: R$")
		leia(marco)
		escreva("Seu total de vendas em abril: R$")
		leia(abril)

		total = (janeiro+fevereiro+marco+abril)
		media = (janeiro+fevereiro+marco+abril)/4

		escreva("O vendedor " + nome + " obteve um total de R$ " + total + " em vendas, com uma média de R$ " + media)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 601; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */