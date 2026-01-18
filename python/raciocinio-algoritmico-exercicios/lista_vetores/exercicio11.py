# Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encon-
# tram o maior e o menor valor

vetor = []
indice = 0

while indice < 5:

    numero = int(input(f"Digite o {indice +1 }º número (5 no total): "))
    vetor.append(numero)
    indice += 1

indice = 0
maior_numero = vetor[0]
posicao_maior_numero = 0
menor_numero = vetor[0]
posicao_menor_numero = 0

while indice < 5:

    if vetor[indice] > maior_numero:

        maior_numero = vetor[indice]
        posicao_maior_numero = indice + 1

    if vetor[indice] < menor_numero:

        menor_numero = vetor[indice]
        posicao_menor_numero = indice + 1

    indice += 1

print(f"Números: {vetor}.\nMaior número: {maior_numero}.\nPosição do maior número: {posicao_maior_numero}º.\nMenor número: {menor_numero}.\nPosição menor número: {posicao_menor_numero}º.")