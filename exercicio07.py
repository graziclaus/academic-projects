# Escreva um programa que crie uma lista com os números de 1 a 100. Em seguida,
# imprima apenas os números pares da lista.

lista_numeros_pares = []

for index in range(1,101):

    if index % 2 == 0:

        lista_numeros_pares.append(index)

print(f"Lista com números pares: {lista_numeros_pares}.")