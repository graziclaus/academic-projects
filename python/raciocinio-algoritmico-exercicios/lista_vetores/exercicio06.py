# Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá
# ser impresso o maior e o menor elemento do vetor

vetor = []
indice = 0

while indice < 10:

    numero = int(input(f"Digite o {indice +1 }º número (10 no total): "))
    vetor.append(numero)
    indice += 1

indice = 0
maior_numero = vetor[0]
menor_numero = vetor[0]

while indice < 10:

    if vetor[indice] > maior_numero:

        maior_numero = vetor[indice]

    if vetor[indice] < menor_numero:

        menor_numero = vetor[indice]

    indice += 1

print(f"Números: {vetor}.\nMaior número: {maior_numero}.\nMenor número: {menor_numero}.")

# 1º vetor[0] (2) > maior_numero (3) = falso; vetor[0] (3) < menor_numero (3) = falso --> maior = 2 menor = 2
# 2º vetor[1] (6) > maior_numero (2) = verdadeiro; vetor[1] (6) < menor_numero (2) = falso   --> maior = 6 menor = 2....