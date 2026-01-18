# Exercício 04

# Crie uma função chamada contar_caracteres que receba uma string e um
# caractere como parâmetros e retorne o número de vezes que o caractere
# aparece na string

def contar_caracteres(string, caracter):

    return string.count(caracter)

numero_vezes_repetidas = contar_caracteres("eu amo abacates","a")
print(f"Número de vezes em que o caracter se repetiu: {numero_vezes_repetidas}")