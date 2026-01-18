# Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
# juntamente com o maior, o menor e a média dos valores.

indice = 0
vetor = []
soma = 0

while indice < 5:

    numero = int(input(f"Digite o {indice + 1 }º número (5 no total): "))
    vetor.append(numero)
    soma += numero
    indice += 1

indice = 0
maior_numero = vetor[0]
menor_numero = vetor[0]

while indice < 5:

    if vetor[indice] > maior_numero:

        maior_numero = vetor[indice]

    if vetor[indice] < menor_numero:

        menor_numero = vetor[indice]

    indice += 1

media_valores = soma/5

print(f"Números: {vetor}.\nMaior número: {maior_numero}.\nMenor número: {menor_numero}.\nMédia dos valores: {media_valores}.")