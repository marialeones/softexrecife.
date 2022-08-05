"""Construa um algoritmo de ordenação, utilizando o método bubble sort estudado. (Lembre-se que se trata de uma série 
de instruções que devem ser seguidas passo a passo).
Para isso, você deve criar um método em que o tamanho do vetor seja dez e deve estar em ordem crescente.
O vetor deverá:
- comparar seus elementos dois a dois adjacentes;
- se os elementos não estiverem em ordem, então ordenar;
- senão, avançar para o próximo par;
- repetir a operação até que nenhuma troca possa ser feita no vetor inteiro."""

import random

def bubble_sort(v):
    fim = len(v)
    while fim > 0:
        i = 0
        while i < fim-1:
            if v[i] > v[i+1]:
                tempo = v[i]
                v[i] = v[i+1]
                v[i+1] = tempo
                print(v)
            i += 1
        fim -= 1




vetor = list(range(0,10))
random.shuffle(vetor)
print(vetor)
print("\n")

bubble_sort(vetor)
print("\n")
print(vetor)



