# Fazer um programa para encontrar todos os números pares entre 1 e 100.

numeros_pares = 0
numeros_impares = 0

for numeros in range(1,101):

    if numeros % 2 != 0:

        numeros_pares += 1

    else:

        numeros_impares += 1

print(f"Números pares: {numeros_pares}.\nNúmeros ímpares: {numeros_impares}")