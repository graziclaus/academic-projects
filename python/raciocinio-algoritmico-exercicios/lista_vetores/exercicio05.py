# Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.

indice = 0
vetor = []
quantidade_numero_par = 0

while indice < 10:

    numeros = int(input(f"Digite o {indice + 1}º número (10 no total): "))
    vetor.append(numeros)

    if numeros % 2 == 0:

        quantidade_numero_par += 1

    indice += 1

print(f"Números digitados: {vetor}.\nQuantidade de números pares: {quantidade_numero_par}.")