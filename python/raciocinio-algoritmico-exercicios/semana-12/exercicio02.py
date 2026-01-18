# Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a
# coluna) do maior valor.

matriz = [

    [0] * 4,
    [0] * 4,
    [0] * 4,
    [0] * 4

]

for linha in range(4):

    for coluna in range(4):

        numeros = int(input(f"Digite o número para a {linha + 1}º, {coluna + 1}º: "))
        matriz[linha][coluna] = numeros

maior = matriz[0][0]
localizacao_linha = 0
localizacao_coluna = 0

for linha in range(4):

    print(f"{linha + 1}º linha da matriz: {matriz[linha]}\n")

for linha in range(4):

    for coluna in range(4):

        if matriz[linha][coluna] > maior:

            maior = matriz[linha][coluna]
            localizacao_linha = linha
            localizacao_coluna = coluna

print(f"Maior número: {maior}.\nLinha do maior número: {localizacao_linha + 1}.\nColuna do maior valor: {localizacao_coluna + 1}")