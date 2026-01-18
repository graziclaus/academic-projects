# Escreva um programa que crie uma lista de palavras e imprima a palavra mais
# longa e a palavra mais curta da lista.

lista_palavras = ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]

palavra_mais_longa = max(lista_palavras, key=len)
palavra_mais_curta = min(lista_palavras, key=len)

print(f"Lista de palavras: {lista_palavras}.\nPalavra mais longa: {palavra_mais_longa}.\nPalavra mais curta: {palavra_mais_curta}.")