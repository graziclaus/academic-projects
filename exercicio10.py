# Dado um vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6] imprima o número que se repete
# mais vezes.

# 2 --> 1; 4 --> 1; 7 --> 1; 2 --> 2; 3 --> 1; 3 --> 2; 1 --> 1; 0 --> 1; 2 --> 3; 6 --> 1

vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
numero_mais_repetido = 0
quantidade_repeticoes = 0

for index in range(len(vetor)):

    numero = vetor[index]
    contador = 0

    for index_numeros_repetidos in range(len(vetor)):

        if vetor[index_numeros_repetidos] == numero:

            contador += 1

    if contador > quantidade_repeticoes:

        numero_mais_repetido = numero
        quantidade_repeticoes = contador

print(f"Número mais repetido: {numero_mais_repetido}\nQuantidade de repetições: {quantidade_repeticoes}")