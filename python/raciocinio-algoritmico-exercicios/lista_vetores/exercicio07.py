# Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima
# o vetor, o maior elemento e a posição que ele se encontra

vetor = []
indice = 0

while indice < 10:

    numero = int(input(f"Digite o {indice + 1}º número (10 no total): "))
    vetor.append(numero)
    indice += 1

indice = 0
indice_maior = 0
maior_numero = vetor[0]

while indice < 10:

    if vetor[indice] > maior_numero:

        maior_numero = vetor[indice]
        indice_maior = indice

    indice += 1

print(f"Números: {vetor}.\nMaior número: {maior_numero}.\nPosição do maior número: {indice_maior + 1}º posição.")