# Escreva um programa que crie uma lista com as letras do alfabeto e embaralhe
# suas posições. Em seguida, peça ao usuário para adivinhar a posição correta de
# uma determinada letra e informe se ele acertou ou errou.

import random
import string
from string import ascii_letters, ascii_lowercase

lista_alfabeto = list(ascii_lowercase)

random.shuffle(lista_alfabeto)
letra_misteriosa = random.choice(lista_alfabeto)

escolha_usuario = int(input(f"A letra da vez é '{letra_misteriosa}', consegue adivinhar onde que ela está?\nAdivinhe sua posição (0 a 25)!: "))

if escolha_usuario == lista_alfabeto.index(letra_misteriosa):

    print(f"Você acertou! A letra '{letra_misteriosa}' estava na posição '{lista_alfabeto.index(letra_misteriosa)}'!")

else:

    print(f"Quase! A letra '{letra_misteriosa}' estava na posição '{lista_alfabeto.index(letra_misteriosa)}'.")

print(lista_alfabeto)