# Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
# e imprima a média geral.

indice = 0
notas_alunos = []
soma = 0

while indice < 15:

    nota = float(input(f"Digite a nota do {indice + 1}º aluno: "))
    notas_alunos.append(nota)
    soma += nota
    indice += 1

media_geral = soma/15

print(f"A média geral dos 15 alunos é: {media_geral}.")