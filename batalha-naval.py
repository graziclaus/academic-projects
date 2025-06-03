import re
import shutil
import random

mar = "🌊"

# -------------------------------------------------------------- Montando o tamanho do tabuleiro --------------------------------------------------------------

def tabuleiro():

    return [[mar for _ in range(10)] for _ in range(10)]


# -------------------------------------------------------------- Personalização --------------------------------------------------------------
def tabuleiro_personalizacao(tamanho_matriz_tabuleiro):

    largura_terminal = shutil.get_terminal_size().columns

    for index, linha in enumerate(tamanho_matriz_tabuleiro):

        linha_formatada = ' \033[31m│\033[0m '.join(linha)
        espacos = max((largura_terminal - len(re.sub(r"\033\[[0-9;]*m", "", linha_formatada.strip()))) // 2, 0)
        print(' ' * espacos + linha_formatada)

        if index == 4:

            linha_horizontal = ' \033[31m―\033[0m ' * (len(linha) * 2 - 1)
            espacos = max((largura_terminal - len(re.sub(r"\033\[[0-9;]*m", "", linha_horizontal.strip()))) // 2, 0)
            print(' ' * espacos + linha_horizontal.strip())

        elif index < len(tamanho_matriz_tabuleiro) - 1:

            linha_horizontal = ' \033[36m―\033[0m ' * (len(linha) * 2 - 1)
            espacos = max((largura_terminal - len(re.sub(r"\033\[[0-9;]*m", "", linha_horizontal.strip()))) // 2, 0)
            print(' ' * espacos + linha_horizontal.strip())


# ^ tudo decoração do tabuleiro feito pelo chatgpt
# re é módulo de expressões regulares do Python, serve pra fazer buscas e substituições em texto usando padrões, tipo “achar tudo que bate com essa regra”

# -------------------------------------------------------------- Montando onde cada barco vai ficar --------------------------------------------------------------

def posicao_tropas(tamanho_matriz_tabuleiro):

    # Dicionários para facilitar a vida, tenho a variável e o tamanho dela em uma só lista
    tamanhos_navios = {

        'porta_avioes': 5,
        'navio_tanque': 4,
        'contratorpedeiro': 3,
        'submarino': 2,
        'destroier': 1

    }

    emojis_navios = {

        'porta_avioes': '🛫',
        'navio_tanque': '🛢️',
        'contratorpedeiro': '⛴️',
        'submarino': '🤿',
        'destroier': '🛥️'

    }

    areas = {

        'area_computador': {'linhas': range(0, 4), 'colunas': range(0, 5)},
        'area_jogador': {'linhas': range(5, 9), 'colunas': range(0, 5)},
    }

    posicoes_utilizadas = []

    # Para cada nome e tamanho em tamanhos_navios, retorno a chave (Ex: porta_avioes) e o valor (Ex: 5) dele.
    for nome, tamanho in tamanhos_navios.items():

        posicao_possibilidades = []

        # Para cada linha no tamanho da tamanho_matriz_tabuleiro
        for linha in range(len(tamanho_matriz_tabuleiro)):

            # Para cada coluna no tamanho da tamanho_matriz_tabuleiro
            for coluna in range(len(tamanho_matriz_tabuleiro)):

                # verifica em cada coluna e linha, se o navio pode ficar e não vai exceder o tamanho da matriz
                if coluna + tamanho <= 10:

                    posicao_horizontal = [(linha, coluna + index) for index in range(tamanho)]
                    posicao_possibilidades.append(posicao_horizontal)

                if linha + tamanho <= 10:

                    posicao_vertical = [(linha + index, coluna) for index in range(tamanho)]
                    posicao_possibilidades.append(posicao_vertical)

        # coloca o navio em algum lugar aleatório

        if posicao_possibilidades:

            posicao_escolhida = random.choice(posicao_possibilidades)

            emoji_display_posicao = emojis_navios[nome]
            # para cada linha e coluna na posicao_escolhida, coloco o emoji de cada barco respectivo e seu tamanho na linha e/ou coluna
            for linha, coluna in posicao_escolhida:
                tamanho_matriz_tabuleiro[linha][coluna] = emoji_display_posicao
                posicoes_utilizadas.append((linha, coluna))

# fazer com que as aleatoriedades do barco reflitam uma em cada área corretamente

# def escolha_jogador(tamanho_matriz_tabuleiro):



# def escolha_computador(tamanho_matriz_tabuleiro):


def main():

    tamanho_matriz_tabuleiro = tabuleiro()
    posicao_tropas(tamanho_matriz_tabuleiro)
    tabuleiro_personalizacao(tamanho_matriz_tabuleiro)
# escolha_jogador(tamanho_matriz_tabuleiro)
#    escolha_computador(tamanho_matriz_tabuleiro)


main()
# Funções: tabuleiro, posição, verificar posição, fazer jogada (computador e player),