# Exercício 02

# Crie uma função chamada e_palindromo que receba uma string como
# parâmetro e retorne True se a string for um palíndromo (ou seja, se lida de trás
# para frente for igual à original) e False caso contrário.

def e_palindromo(string):
    string_invertida = string[::-1]

    if string == string_invertida:

        string_igual = True

    else:

        string_igual = False

    return string_igual


resultado_1 = e_palindromo("ana")
resultado_2 = e_palindromo("bicicleta")

print(f"Primeiro resultado: {resultado_1}\nSegundo resultado: {resultado_2}")