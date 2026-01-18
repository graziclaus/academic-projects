# Dado um vetor A de tamanho N e um vetor B de tamanho N, crie um programa
# que calcule a soma dos elementos desses vetores e armazene o resultado em
# um vetor C de tamanho N. Regras:
# a. O tamanho dos vetores A, B e C é fornecido pelo usuário.
# b. Os elementos dos vetores A e B são fornecidos pelo usuário.

tamanho_vetores = int(input("Digite o tamanho para os vetores A, B e C: "))

vetor_A = [0] * tamanho_vetores
vetor_B = [0] * tamanho_vetores
vetor_C = [0] * tamanho_vetores

for index in range(tamanho_vetores):

    vetor_A[index] = int(input(f"Digite o {index + 1}º número para o Vetor A: "))

for index in range(tamanho_vetores):

    vetor_B[index] = int(input(f"Digite o {index + 1}º número para o Vetor B: "))

for index in range(tamanho_vetores):

    vetor_C[index] = vetor_A[index] + vetor_B[index]

print(f"Vetor C (soma dos vetores A e B): {vetor_C}")

# Teste de Mesa