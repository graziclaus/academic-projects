# Exercício 03

# Crie uma função chamada maior_elemento que receba uma lista de números
# como parâmetro e retorne o maior elemento dessa lista.

# def maior_elemento(numeros):
#    return max(numeros)

def maior_elemento(numeros):
    maior = numeros[0]

    for index in range(len(numeros)):

        if numeros[index] > maior:
            maior = numeros[index]

    return maior


print(maior_elemento([5, 432234423, 1]))