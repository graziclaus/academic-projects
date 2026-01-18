# Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a
# tabuada de 1 a 10 do valor lido.

numero = int(input(f"Digite um número para imprimir a tabuada: "))

for multiplicador in range(1,11):

    total = numero * multiplicador

    print(f"{numero} x {multiplicador} = {total}")
