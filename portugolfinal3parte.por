programa
{
	
	funcao inicio()
	{
	cadeia aereo
     cadeia pular
     cadeia viaja
     cadeia devagar
     cadeia piloto
     cadeia asas
     cadeia voo
	
		escreva("o veículo e aéreo? ")
		leia(aereo)
		se(aereo == "sim") {
			escreva("é preciso pular? ")
			leia(pular)
			se(pular == "sim") {
				escreva("==> É ASA DELTA <==")
			}senao se(pular == "nao") {
			   escreva("viaja dentro? ")
			   leia(viaja)
			   se(viaja == "sim") {
			   	escreva("é devagar? ")
			   	leia(devagar)
			   	se(devagar == "sim") {
			   		escreva("==> É UM BALÃO <==")
			   	}senao se(devagar == "nao") {
			   		escreva("tem piloto? ")
			   		leia(piloto)
			   		se(piloto == "sim") {
			   			escreva("possui asas fixas? ")
			   			leia(asas)
			   			se(asas == "sim") { 
			   				escreva("==> É UM AVIÃO <==")
			   			}senao se(asas == "nao") {
			   				escreva("faz voo vertical? ")
			   				leia(voo)
			   				se(voo == "sim") {
			   					escreva("==> É UM HELICÓPTERO <==")
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
 * @POSICAO-CURSOR = 782; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */