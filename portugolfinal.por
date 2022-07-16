programa
{
	
	funcao inicio()
	{
	cadeia veiculo
	cadeia pessoa
	cadeia pesado
	cadeia pedal
	cadeia capacete
	cadeia passageiro
	cadeia trilho
	cadeia pista
	cadeia alto
	cadeia carroceria
	cadeia cobrador
	cadeia leve
	
		escreva("o veículo e terreste? ")
		leia(veiculo)
		se(veiculo == "sim") {
			escreva("cade apenas uma pessoa? ")
			leia(pessoa)
			se(pessoa == "sim") {
				escreva("é pesado? ")
				leia(pesado)
				se(pesado == "sim") {
					escreva(" ==> É UM TRATOR <== ") 
				}senao se(pesado == "nao") {
					escreva("tem pedal? ")
					leia(pedal)
					se(pedal == "sim") {
						escreva("==> É UMA BICICLETA <==") 
					}senao se(pessoa == "nao") {
						escreva("usa capacete? ")
						leia(capacete)
						se(capacete == "sim") {
							escreva("==> É UMA MOTO <==")
						}senao  {
							escreva("tem passageiro? ")
							leia(passageiro)
							se(passageiro == "sim") {
								escreva("usa trilho? ")
								leia(trilho)
								se(trilho == "sim") {
									escreva("==> É UM TREM <==")
								}senao se(trilho == "nao"){
									escreva("anda na pista? ")
									leia(pista)
									se(pista == "sim") {
										escreva("e alto? ")
										leia(alto)
										se(alto == "sim") {
											escreva("usa carroceria? ")
											leia(carroceria)
											se(carroceria == "sim") {
												escreva("==> É UM CAMINHÃO <==")
											}senao se(carroceria == "nao") {
												escreva("pode ter cobrador? ")
												leia(cobrador)
												se(cobrador == "sim") {
													escreva("==> É UM ÔNIBUS <==")
												}senao se(alto == "nao") {
													escreva("é um veículo leve? ")
													leia(leve)
													se(leve == "sim") {
														escreva("==> É UM CARRO <==") 
													}
												}
												
											}
											
										}
										
									}
									
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
 * @POSICAO-CURSOR = 806; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */