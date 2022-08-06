"""Tamanho do vetor: 30;
- Utilize números ímpares;
- Opere em ordem crescente."""
import random

def insertionSort(v):
    i = 1
    while i < len(v):
        temporaria = v[i]
        trocou = False
        n = i - 1
        while n >= 0 and v[n] > temporaria:
            v[n+1] = v[n]
            trocou = True
            n -= 1

        if trocou:
            v[n+1] = temporaria

        i += 1

vetor = list(range(0,30))
random.shuffle(vetor)

insertionSort(vetor)
print(vetor)
