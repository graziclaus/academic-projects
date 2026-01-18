# Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois va-
# lores X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa
# deverá escrever a soma dos valores encontrados nas respectivas posições X e Y

indice = 0
vetor = []


while indice < 8:

    numeros = int(input(f"Digite o {indice + 1}º número (8 no total): "))
    vetor.append(numeros)
    indice += 1

while True:

    valor_x = int(input("Digite a posição X (0 a 7) para realizar a soma: "))
    valor_y = int(input("Digite a posição Y (0 a 7) para realizar a soma: "))

    if (0 <= valor_x <= 7) and (0 <= valor_y <= 7):

        soma = vetor[valor_x] + vetor[valor_y]

        print(f"Números: {vetor}.")
        print(f"Número da posição X: {vetor[valor_x]}º.\nNúmero da posição Y: {vetor[valor_y]}º.")
        print(f"Soma dos números da posição {valor_x} (X) e da posição {valor_y} (Y): {soma}.")
        break

    else:

        print("Posição inválida, tente novamente!")