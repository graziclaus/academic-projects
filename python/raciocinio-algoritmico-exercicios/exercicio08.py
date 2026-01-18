# Faça um algoritmo que leia 10 números inteiros, armazene-os em um vetor e
# imprima em ordem crescente.

numeros = [0] * 10

for index in range(10):

    numeros[index] = int(input(f"Digite o {index + 1}º número: "))

for index in range(10):

    for segundo_index in range(index + 1, 10):

        if numeros[segundo_index] < numeros[index]:

            # a,b = b,a -> troca valores --> 1, 5 = 5,1
            numeros[index], numeros[segundo_index] = numeros[segundo_index], numeros[index]

print(f"Números em ordem crescente: {numeros}")
