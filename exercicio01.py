# Escreva um programa que crie uma lista com números aleatórios e a imprima na
# tela.

import random

lista_aleatoria = []

for index in range(5):

    numeros_aleatorios = random.randint(0, 10)
    lista_aleatoria.append(numeros_aleatorios)

print(f"Lista com números aleatórios: {lista_aleatoria}")