# Se você terminou os exercícios acima. Tente agora fazer o jogo da velha, mas
# utilizando listas.

import random

tabuleiro = [" "] * 9
rodadas = 0
combinacoes_jogadas = [

    [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]

]

# -------------------------------------------------------- Modos --------------------------------------------------------

modo = input("Vamos jogar jogo da velha?\nEscolha seu modo (PvP), (PvC), (CvC)!: ").lower()

while modo in ["pvp", "pvc", "cvc"]:

    vez = input("Quem você deseja ser, 'X' ou 'O'?").upper()

    while vez != "X" and vez != "O":

        print("Opção inválida! Tente novamente.")
        vez = input("Com o que você deseja começar, 'X' ou 'O'?: ").upper()

    jogador = vez

# ------------------------ Modo PvP ------------------------

    while modo == "pvp":

        print(f"  {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}\n"
              f"  ---------\n"
              f"  {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}\n"
              f"  ---------\n"
              f"  {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

        escolha_jogador = int(input(f"Player '{vez}'! Digite a posição que você quer jogar (0 a 8): "))

        if escolha_jogador < 0 or escolha_jogador > 8 or tabuleiro[escolha_jogador] != " ":

            print("Jogada inválida ou a posição está ocupada. Tente novamente.")
            continue

        tabuleiro[escolha_jogador] = vez
        rodadas += 1

        for jogada in combinacoes_jogadas:

            if tabuleiro[jogada[0]] == tabuleiro[jogada[1]] == tabuleiro[jogada[2]] != " ":

                print(f"  {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}\n"
                      f"  ---------\n"
                      f"  {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}\n"
                      f"  ---------\n"
                      f"  {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

                print(f"\nResultado da partida: o jogador '{vez}' venceu!")
                exit()

        if vez == "X":

            vez = "O"

        else:

            vez = "X"

        if rodadas == 9:

            print("Resultado da partida: deu velha!")
            exit()

# ------------------------ Modo PvC ------------------------

    while modo == "pvc":

        print(f"  {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}\n"
              f"  ---------\n"
              f"  {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}\n"
              f"  ---------\n"
              f"  {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")


        if vez == jogador:

            escolha_jogador_computador = int(input(f"Player '{vez}'! Digite a posição que você quer jogar (0 a 8): "))

            if escolha_jogador_computador < 0 or escolha_jogador_computador > 8 or tabuleiro[escolha_jogador_computador] != " ":

                print("Jogada inválida ou a posição está ocupada. Tente novamente.")
                continue

        else:

            print("Rodada do computador!")

            posicoes_livres = []
            for index in range(9):

                if tabuleiro[index] == " ":

                    posicoes_livres.append(index)

            escolha_jogador_computador = random.choice(posicoes_livres)
            print(f"O computador escolheu a posição: {escolha_jogador_computador}")

        tabuleiro[escolha_jogador_computador] = vez
        rodadas += 1

        for jogada in combinacoes_jogadas:

            if tabuleiro[jogada[0]] == tabuleiro[jogada[1]] == tabuleiro[jogada[2]] != " ":

                print(f"  {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}\n"
                      f"  ---------\n"
                      f"  {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}\n"
                      f"  ---------\n"
                      f"  {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

                print(f"\nResultado da partida: o jogador '{vez}' venceu!")
                exit()

        if vez == "X":

            vez = "O"

        else:

            vez = "X"

        if rodadas == 9:

            print("Resultado da partida: deu velha!")
            exit()

# ------------------------ Modo CvC ------------------------

    while modo == "cvc":

        print(f"  {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}\n"
              f"  ---------\n"
              f"  {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}\n"
              f"  ---------\n"
              f"  {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

        posicoes_livres = []

        for index in range(9):

            if tabuleiro[index] == " ":

                posicoes_livres.append(index)

        if len(posicoes_livres) == 0:

            print("Resultado da partida: deu velha!")
            break

        escolha_computador = random.choice(posicoes_livres)

        print(f"Computador '{vez}'! Digite a posição que você quer jogar (0 a 8):\nComputador '{vez}: eu escolho {escolha_computador}!'")

        tabuleiro[escolha_computador] = vez
        rodadas += 1

        for jogada in combinacoes_jogadas:

            if tabuleiro[jogada[0]] == tabuleiro[jogada[1]] == tabuleiro[jogada[2]] != " ":
                print(f"  {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}\n"
                      f"  ---------\n"
                      f"  {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}\n"
                      f"  ---------\n"
                      f"  {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

                print(f"\nResultado da partida: o jogador '{vez}' venceu!")
                exit()

        if rodadas % 2 == 0:

            vez = "O"

        else:

            vez = "X"

        if rodadas == 9:

            print("Resultado da partida: deu velha!")
            exit()