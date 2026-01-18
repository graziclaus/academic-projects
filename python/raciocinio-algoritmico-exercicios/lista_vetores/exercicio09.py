# Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a
# quantidade de números negativos e a soma dos números positivos desse vetor.

indice = 0
vetor_numeros_reais = []
quantidade_numero_negativo = 0
soma_positivos = 0

while indice < 10:

    numeros_reais = float(input(f"Digite o {indice + 1}º número: "))
    vetor_numeros_reais.append(numeros_reais)

    if numeros_reais < 0:

        quantidade_numero_negativo += 1

    if numeros_reais > 0:

        soma_positivos += numeros_reais

    indice += 1

print(f"Números: {vetor_numeros_reais}.\nQuantidade de números negativos: {quantidade_numero_negativo}.\nSoma dos números positivos: {soma_positivos}.")
