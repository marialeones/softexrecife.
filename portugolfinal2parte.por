programa
{
	
	funcao inicio()
	{
	cadeia aquatico
	cadeia coberto
	cadeia navega
	cadeia vela
	cadeia motor
	cadeia alto
	cadeia descoberto
	
		escreva("o veículo é aquático? ")
		leia(aquatico)
		se(aquatico == "sim") {
			escreva("é coberto de água? ")
			leia(coberto)
			se(coberto == "sim"){
				escreva("==> É UM SUBMARINO <==")
			}senao se(coberto == "nao") {
				escreva("navega na água? ")
				leia(navega)
				se(navega == "sim") {
					escreva("possui vela? ")
					leia(vela)
					se(vela == "sim") { 
						escreva("==> É UM BARCO <==")
					}senao se(vela == "nao") {
						escreva("tem motor? ")
						leia(motor)
						se(motor == "sim") {
							escreva("é alto? ")
							leia(alto)
							se(alto == "sim") {
								escreva("==> É UM NAVIO <==")
							}senao se(alto == "nao") {
								escreva("pode ser descoberto? ")
								leia(descoberto) 
								se(descoberto == "sim") {
									escreva("==> É UMA LANCHA <==")
								}
							}
							
						}
					}
				}
				
			}
			
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 948; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */