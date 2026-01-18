# Exercício 05

# Implemente uma calculadora simples em Python utilizando funções. A
# calculadora deve ser capaz de realizar as seguintes operações
# matemáticas básicas:
# • Soma
# • Subtração
# • Multiplicação
# • Divisão
# Requisitos:
# • Crie uma função para cada operação matemática (soma,
# subtração, multiplicação e divisão). As funções devem receber
# dois valores e retornar o resultado da operação.
# • Implemente uma função para exibir o menu de opções para o
# usuário.
# • O programa deve repetir o menu após cada operação, até que
# o usuário escolha a opção de sair.

def menu():

    print("Bem-vindo! Sou uma calculadora, temos 4 opções: soma, subtração, multiplicação e divisão!\n")

    while True:

        operacao = input("Digite qual operação matemática você deseja fazer: ").lower()

        if operacao == "sair":

            print("Fim das operações na calculadora. Adeus!")

            break

        if operacao in ["soma", "subtracao", "multiplicacao", "divisao"]:

            numero_um = int(input("Digite o 1º número!: "))
            numero_dois = int(input("Digite o 2º número!: "))

            if operacao == "soma":

                print(soma(numero_um, numero_dois))

            if operacao == "subtracao":

                print(subtracao(numero_um, numero_dois))

            if operacao == "multiplicacao":

                print(multiplicacao(numero_um, numero_dois))

            if operacao == "divisao":

                if numero_dois == 0:

                    print("Não é possível dividir por zero!")

                else:

                    print(divisao(numero_um, numero_dois))

        else:

            print("Operação inválida. Tente: soma, subtracao, multiplicacao, divisao ou sair.")

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

menu()