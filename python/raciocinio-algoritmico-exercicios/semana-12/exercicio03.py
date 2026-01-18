# Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo as
# seguintes informações sobre alunos de uma disciplina, sendo todas as
# informações do tipo inteiro:
# a. Primeira coluna: número de matrícula (use um inteiro)
# b. Segunda coluna: media das provas
# c. Terceira coluna: media dos trabalhos
# d. Quarta coluna: nota final
# Elabore um programa que:
# a. Leia as três primeiras informações de cada aluno;
# b. Calcule a nota final como sendo a soma da média das provas e da
# média dos trabalhos;
# c. Imprima a matrícula do aluno que obteve a maior nota final (assuma que só existe
# uma maior nota).

matriz = [

    [0] * 4,
    [0] * 4,
    [0] * 4,
    [0] * 4,
    [0] * 4

]

for linha in range(5):

    numeros_matricula_alunos = int(input(f"Digite o número da matrícula do {linha + 1}º aluno: "))
    media_provas_alunos = float(input(f"Digite a média das provas do {linha + 1}º aluno: "))
    media_trabalhos_alunos = float(input(f"Digite a média dos trabalhos do {linha + 1}º aluno: "))

    nota_final_alunos = media_provas_alunos + media_trabalhos_alunos

    matriz[linha][0] = numeros_matricula_alunos
    matriz[linha][1] = media_provas_alunos
    matriz[linha][2] = media_trabalhos_alunos
    matriz[linha][3] = nota_final_alunos

maior_nota = matriz[0][3]
matricula_maior_nota = matriz[0][0]

for linha in range(5):

    if matriz[linha][3] > maior_nota:
    
        maior_nota = matriz[linha][3]
        matricula_maior_nota = matriz[linha][0]

print(f"Matrícula do aluno que obteve a maior nota final: {matricula_maior_nota}.\nNota do aluno: {maior_nota}.")

