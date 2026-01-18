# Escreva um programa que crie uma lista com os números de 1 a 10 e os imprima
# na tela em ordem reversa.

lista = []

for index in range(1,11):

    lista.append(index)

print(f"Lista normal: {lista}")

lista_reversa = list(reversed(lista))

print(f"Lista reversa: {lista_reversa}")

