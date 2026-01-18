# Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.

valores_inteiros = []
indice = 0

while indice < 6:

    valor_usuario = int(input(f"Digite {indice + 1}º valor inteiro (6 no total): "))
    valores_inteiros.append(valor_usuario)

    indice += 1

print(f"Valores inteiros: {valores_inteiros}.")