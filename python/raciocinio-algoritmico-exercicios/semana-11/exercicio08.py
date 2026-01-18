# Escreva um programa que crie uma lista com os números de 1 a 10 elevados ao
# quadrado. Em seguida, calcule a soma dos elementos da lista e imprima o
# resultado.

lista = []

for index in range(1,11):

    index = index**2
    lista.append(index)

print(f"Lista: {lista}")
soma = sum(lista)
print(f"Soma dos elementos da lista: {soma}")