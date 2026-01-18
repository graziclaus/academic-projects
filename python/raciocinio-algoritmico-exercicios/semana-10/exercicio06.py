# Utilizando a estrutura de repetição for, faça um programa que receba 10
# números e conte quantos deles estão no intervalo [10,20] e quantos deles
# estão fora do intervalo.

numeros_dentro_intervalo = 0
numeros_fora_intervalo = 0
numeros = [0] * 10

for index in range(10):

    numeros[index] = int(input(f"Digite o {index + 1}º número: "))

    if 10 <= numeros[index] <= 20:

        numeros_dentro_intervalo += 1

    else:

        numeros_fora_intervalo += 1

print(f"Números dentro do intervalo 10 a 20: {numeros_dentro_intervalo}.\nNúmeros fora do intervalo 10 a 20: {numeros_fora_intervalo}.")

