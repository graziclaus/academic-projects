# Faça um algoritmo que solicita ao usuário um texto qualquer. Calcule quantas
# vogais existem no texto. Imprima quais vogais existem no texto e quantas são.

quantidade_vogais = 0

texto = input("Digite um texto qualquer: ").lower()

vogais = ["a", "e", "i", "o", "u"]
vogal_a = vogal_e = vogal_i = vogal_o = vogal_u = False

for letra in texto:

    if letra == "a":

        quantidade_vogais += 1
        vogal_a = True

    if letra == "e":

        quantidade_vogais += 1
        vogal_e = True

    if letra == "i":

        quantidade_vogais += 1
        vogal_i = True

    if letra == "o":

        quantidade_vogais += 1
        vogal_o = True

    if letra == "u":

        quantidade_vogais += 1
        vogal_u = True

print(f"Quantidade de vogais: {quantidade_vogais}.\nVogais que existem no texto: ")

if vogal_a:

    print("a")

if vogal_e:

    print("e")

if vogal_i:

    print("i")

if vogal_o:

    print("o")

if vogal_u:

    print("u")

