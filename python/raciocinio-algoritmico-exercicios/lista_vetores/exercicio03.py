# Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das
# componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10
# elementos cada. Imprimir os conjuntos.

indice = 0
numeros_reais = []
quadrado_numeros_reais = []

while indice < 10:

    numeros_reais_usuario = float(input(f"Digite o {indice + 1}º número (10 no total): "))
    numeros_reais.append(numeros_reais_usuario)
    quadrado_numeros_reais.append(numeros_reais_usuario ** 2)
    indice += 1

print(f"Números reais: {numeros_reais}.\nNúmeros reais ao quadrado: {quadrado_numeros_reais}.")