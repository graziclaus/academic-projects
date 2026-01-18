# Ler 10 números e imprimir quantos são pares e quantos são ímpares.

numeros = [0] * 10
numeros_pares = 0
numeros_impares = 0

for index in range(10):

    numeros[index] = int(input(f"Digite o {index + 1}º número: "))

    if numeros[index] % 2 == 0:

        numeros_pares += 1

    else:

        numeros_impares += 1

print(f"Números pares: {numeros_pares}.\nNúmeros ímpares: {numeros_impares}")