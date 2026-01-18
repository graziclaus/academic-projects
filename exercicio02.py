# Escreva um programa que peça ao usuário três números e os armazene em uma
# lista. Em seguida, imprima a lista na tela.

lista_usuario = []

for index in range(3):

    numeros = int(input(f"Digite os {index + 1}º número: "))
    lista_usuario.append(numeros)

print(f"Lista: {lista_usuario}.")