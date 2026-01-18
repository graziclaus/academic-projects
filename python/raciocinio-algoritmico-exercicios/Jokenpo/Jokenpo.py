# Biblioteca importada para criar aleatoriedade nas escolhas de modos que tenham bots
import random

# Introdução ao jogo e menu principal
print("######JOKENPÔ######")
print("---------------------------------- // ----------------------------------")
print("\033[1mRegras do Jokenpô!\033[0m\nVocê possui \033[4mtrês escolhas\033[0m: pedra, papel ou tesoura.\n")
print("\033[1mComo ganhar?:\033[0m Quem joga pedra vence de tesoura, tesoura vence de papel e papel vence de pedra.")
print("\033[1mOpções de jogo:\033[0m Player vs Player (PvP) = 1, Player vs Computador (PvC) = 2 e Computador vs Com"
      "putador (CvC) = 3.")
print("---------------------------------- // ----------------------------------")
modo = input("Digite seu modo de jogo (1, 2 ou 3): \n")

# Variáveis do placar
pontuacao1 = 0
pontuacao2 = 0

# Programa continua rodando mesmo se o usuário digitar o modo incorretamente. Sem o input modo, o programa vai repetir infinitamente o input acima. Não é recomendado tirar
# Funciona como uma catraca impedindo o usuário de entrar com o input errado.
while modo != "1" and modo != "2" and modo != "3":

    print("Esse modo não existe! Tente novamente.")
    modo = input("Digite seu modo de jogo (1, 2 ou 3): \n")

# Modo 1 é Jogador vs Jogador
while modo == "1":

    jogador1 = input("Jogador 1, jogue pedra, papel ou tesoura: ")

    jogador2 = input("Jogador 2, jogue pedra, papel ou tesoura: ")


    if (jogador1.lower() != "pedra" and jogador1.lower() != "papel" and jogador1.lower() != "tesoura") or (jogador2.lower() != "pedra" and jogador2.lower() != "papel" and jogador2.lower() != "tesoura"):
        
        print("Por favor, selecione uma jogada válida.")
        # Continua o loop até que o usuário acerte as palavras necessárias. Poderia deixar sem o continue, mas então, aparecia o "CONTINUAR" ou "SAIR" toda vem
        # que digitasse algo errado.
        # continue irá ignorar o erro e vai voltar no loop

        continue

# Escolhas e Resultados
    elif jogador1.lower() == jogador2.lower():

        print("\033[1mEMPATE!!!\033[0m")
        print(str(pontuacao1) + " - "  + str(pontuacao2))

    elif jogador1.lower() == 'pedra' and jogador2.lower() == "tesoura":

        print("\033[1mjogador1 venceu a rodada\033[0m")
        pontuacao1 += 1
        print(str(pontuacao1) + " - "  + str(pontuacao2))

    elif jogador1.lower() == 'tesoura' and jogador2.lower() == 'papel':

        print("\033[1mjogador1 venceu a rodada\033[0m")
        pontuacao1 += 1
        print(str(pontuacao1) + " - " + str(pontuacao2)) 

    elif jogador1.lower() == 'papel' and jogador2.lower() == 'pedra':

        print("\033[1mjogador1 venceu a rodada\033[0m")
        pontuacao1 += 1
        print(str(pontuacao1) + " - " + str(pontuacao2))

# ----------------------------------   ----------------------------------   ----------------------------------   ----------------------------------   

    elif jogador2.lower() == 'pedra' and jogador1.lower() == 'tesoura':

        print("\033[1mjogador2 venceu a rodada\033[0m")
        pontuacao2 += 1
        print(str(pontuacao1)+ " - " + str(pontuacao2))

    elif jogador2.lower() == 'tesoura' and jogador1.lower() == 'papel':

        print("\033[1mjogador2 venceu a rodada\033[0m")
        pontuacao2 += 1
        print(str(pontuacao1) + " - " + str(pontuacao2))

    elif jogador2.lower() == 'papel' and jogador1.lower() == 'pedra':

        print("\033[1mjogador2 venceu a rodada\033[0m")
        pontuacao2 += 1
        print(str(pontuacao1) + " - " + str(pontuacao2))

# Enquanto continuar e sair for verdadeiro, ele vai sair do loop, caso contrário ele permanecerá no loop até estar correto.
    while True:

        saida = input("Deseja CONTINUAR ou SAIR?\n")

        if saida.lower() == "continuar":

            break

        elif saida.lower() == "sair":

            print("\n")
            print("Placar Final: \n")
            print("Jogador 1 | Jogador 2")
            print("        " + str(pontuacao1) + " - " + str(pontuacao2))
            print("Adeus. Obrigada por testar o nosso programa!!\n")
            print("Participantes: Julia Portela, Edoarda Cenci, Grazielle Claus\n")
            # Se usar o break, vai sair apenas do while da linha 87. Exit é usado para terminar o programa de vez
            exit()

        else:

            print("Algo deu errado. Tente digitar o comando novamente")

# ----------------------------------------------------------------------------------------------------------------------------------------   

while modo == "2":

# pedra = 1, papel = 2, tesoura = 3

    jogador1 = input("Jogue pedra, papel ou tesoura: ")
    jogador2 = random.randint(1,3)

    if jogador1.lower() != "pedra" and jogador1.lower() != "papel" and jogador1.lower() != "tesoura":
        
        print("Por favor, selecione uma jogada válida.")
        continue

    if (jogador1.lower() == "pedra" and jogador2 == 1) or (jogador1.lower() == "papel" and jogador2 == 2) or (jogador1.lower() == "tesoura" and jogador2 == 3):

        print("\033[1mEMPATE!!!\033[0m")
        print(str(pontuacao1) + " - " + str(pontuacao2))

    elif jogador1.lower() == 'pedra' and jogador2 == 3:

        print("jogador2 escolheu tesoura\n")
        print("\033[1mjogador1 venceu a rodada!\033[0m")
        pontuacao1 += 1
        print(str(pontuacao1) + " - "  + str(pontuacao2))

    elif jogador1.lower() == 'tesoura' and jogador2 == 2:

        print("jogador2 escolheu papel\n")
        print("\033[1mjogador1 venceu a rodada\033[0m")
        pontuacao1 += 1
        print(str(pontuacao1) + " - " + str(pontuacao2)) 

    elif jogador1.lower() == 'papel' and jogador2 == 1:

        print("jogador2 escolheu pedra\n")
        print("\033[1mjogador1 venceu a rodada\033[0m")
        pontuacao1 += 1
        print(str(pontuacao1) + " - " + str(pontuacao2))

# ---------------------------------- // ---------------------------------- // ---------------------------------- // ----------------------------------   

    elif jogador2 == 1 and jogador1.lower() == 'tesoura':

        print("jogador2 escolheu pedra\n")
        print("\033[1mjogador2 venceu a rodada\033[0m")
        pontuacao2 += 1
        print(str(pontuacao1)+ " - " + str(pontuacao2))

    elif jogador2 == 3 and jogador1.lower() == 'papel':

        print("jogador2 escolheu tesoura\n")
        print("\033[1mjogador2 venceu a rodada\033[0m")
        pontuacao2 += 1
        print(str(pontuacao1) + " - " + str(pontuacao2))

    elif jogador2 == 2 and jogador1.lower() == 'pedra':

        print("jogador2 escolheu papel\n")
        print("\033[1mjogador2 venceu a rodada\033[0m")
        pontuacao2 += 1
        print(str(pontuacao1) + " - " + str(pontuacao2))

    while True:

        saida = input("Deseja CONTINUAR ou SAIR?\n")

        if saida.lower() == "continuar":

            break

        elif saida.lower() == "sair":

            print("\n")
            print("Placar Final: \n")
            print("Jogador 1 | Jogador 2")
            print("        " + str(pontuacao1) + " - " + str(pontuacao2))
            print("Adeus. Obrigada por testar o nosso programa!!\n")
            print("Participantes: Julia Portela, Edoarda Cenci, Grazielle Claus\n")
            # se usar o break, vai sair apenas do while da linha 91. Exit é usado para terminar o programa de vez
            exit()

        else:

            print("Algo deu errado. Tente digitar o comando novamente")

# ----------------------------------------------------------------------------------------------------------------------------------------   

while modo == "3":

    jogador1 = random.randint(1,3)
    jogador2 = random.randint(1,3)

    if jogador1 == jogador2:

        if jogador1 == 1 and jogador2 == 1:
            print("Ambos jogaram pedra")
        elif jogador1 == 2 and jogador2 == 2:
            print("Ambos jogaram papel")
        elif jogador1 == 3 and jogador2 == 3:
            print("Ambos jogaram tesoura")
        print("\033[1mEMPATE!!!\033[0m")
        print(str(pontuacao1) + " - " + str(pontuacao2))

    elif jogador1 == 1 and jogador2 == 3:

        print("Jogador 1 escolheu pedra")
        print("Jogador 2 escolheu tesoura\n")
        print("\033[1mJogador 1 venceu a rodada\033[0m")
        pontuacao1 += 1
        print(str(pontuacao1) + " - "  + str(pontuacao2))

    elif jogador1 == 3 and jogador2 == 2:

        print("Jogador 1 escolheu tesoura")
        print("Jogador 2 escolheu papel\n")
        print("\033[1mJogador 1 venceu a rodada\033[0m")
        pontuacao1 += 1
        print(str(pontuacao1) + " - " + str(pontuacao2)) 

    elif jogador1 == 2 and jogador2 == 1:

        print("Jogador 1 escolheu papel")
        print("Jogador 2 escolheu pedra\n")
        print("\033[1mJogador 1 venceu a rodada\033[0m")
        pontuacao1 += 1
        print(str(pontuacao1) + " - " + str(pontuacao2))

# ---------------------------------- // ---------------------------------- // ---------------------------------- // ----------------------------------   

    elif jogador2 == 1 and jogador1 == 3:

        print("Jogador 1 escolheu tesoura")
        print("Jogador 2 escolheu pedra\n")
        print("\033[1mJogador 2 venceu a rodada\033[0m")
        pontuacao2 += 1
        print(str(pontuacao1)+ " - " + str(pontuacao2))

    elif jogador2 == 3 and jogador1 == 2:

        print("Jogador 1 escolheu papel")
        print("Jogador 2 escolheu tesoura\n")
        print("\033[1mJogador 2 venceu a rodada\033[0m")
        pontuacao2 += 1
        print(str(pontuacao1) + " - " + str(pontuacao2))

    elif jogador2 == 2 and jogador1 == 1:

        print("Jogador 1 escolheu pedra")
        print("Jogador 2 escolheu papel\n")
        print("\033[1mJogador 2 venceu a rodada\033[0m")
        pontuacao2 += 1
        print(str(pontuacao1) + " - " + str(pontuacao2))

    while True:

        saida = input("Deseja CONTINUAR ou SAIR?\n")

        if saida.lower() == "continuar":

            break

        elif saida.lower() == "sair":

            print("\n")
            print("Placar Final: \n")
            print("Jogador 1 | Jogador 2")
            print("        " + str(pontuacao1) + " - " + str(pontuacao2))
            print("Adeus. Obrigada por testar o nosso programa!!\n")
            print("Participantes: Julia Portela, Edoarda Cenci, Grazielle Claus\n")
            # se usar o break, vai sair apenas do while da linha 91. Exit é usado para terminar o programa de vez
            exit()

        else:

            print("Algo deu errado. Tente digitar o comando novamente")
