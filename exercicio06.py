# Escreva um programa que crie duas listas, uma com os números pares de 1 a 10
# e outra com os números ímpares de 1 a 10. Em seguida, junte as duas listas em
# uma terceira lista e a imprima na tela.

lista_numeros_pares = []
lista_numeros_impares = []

for index in range(1,11):

    if index % 2 == 0:

        lista_numeros_pares.append(index)

    else:

        lista_numeros_impares.append((index))


terceira_lista = lista_numeros_impares + lista_numeros_pares

print(f"Lista com números pares: {lista_numeros_pares}.\nLista com números ímpares: {lista_numeros_impares}.\nLista com todos os números: {terceira_lista}.\nLista ordenada: {sorted(terceira_lista)}")