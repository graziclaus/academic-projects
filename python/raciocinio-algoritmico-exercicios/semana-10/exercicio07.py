# Faça um programa que calcule e mostre a soma dos 50 primeiros números
# pares.

soma = 0
for numeros in range(100):

    if numeros % 2 == 0:

        soma += numeros
        numeros += 1

        if numeros == 50:

            break

print(f"Soma dos primeiros 50 números: {soma}")

