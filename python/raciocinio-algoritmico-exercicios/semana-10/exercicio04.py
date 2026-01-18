# Leia várias idades e calcule a média entre as idades (usar uma variável para
# idade)

media = 0
soma = 0
idade = [0] * 5
for index in range(5):

    idade[index] = int(input(f"Digite a {index + 1}º idade: "))
    soma += idade[index]

media = soma/5
print(f"Idades:{idade}.\nMédia das idades: {media}")