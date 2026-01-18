# Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os
# demais elementos. Escreva ao final a matriz obtida.

matriz = [

    [0] * 5,
    [0] * 5,
    [0] * 5,
    [0] * 5,
    [0] * 5
]

for diagonal in range(5):

    matriz[diagonal][diagonal] = 1

for linha in range(5):
    
    print(matriz[linha])
