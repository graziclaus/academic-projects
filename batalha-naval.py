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

def verificar_posicoes_livres(tamanho_matriz_tabuleiro, posicoes_tropas):

    for linha, coluna in posicoes_tropas:

        if tamanho_matriz_tabuleiro[linha][coluna] != mar:

            return False

    return True

def colocar_navio_tabuleiro(tamanho_matriz_tabuleiro, posicoes_tropas, emoji_navio):

    for linha, coluna in posicoes_tropas:

        tamanho_matriz_tabuleiro[linha][coluna] = emoji_navio

def posicao_tropas(tamanho_matriz_tabuleiro, areas):

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

    # para o nome da area (jogador ou computador) e a area (onde vai campo), dentro do dicionário area
    for nome_area, area in areas.items():

        # colocando os navios, linhas e colunas em uma lista para aleatorizar bem tanto vertical quanto horizontal depois
        navios_lista = list(tamanhos_navios.items())
        random.shuffle(navios_lista)
        # Para cada nome e tamanho em tamanhos_navios, retorno a chave (Ex: porta_avioes) e o valor (Ex: 5) dele.
        for nome, tamanho in tamanhos_navios.items():

            posicoes_possiveis_disponiveis = []

            linhas = list(area['linhas'])
            colunas = list(area['colunas'])
            random.shuffle(linhas)
            random.shuffle(colunas)

            # pega da onde vai tal linha (0-5 ou 0-5)
            for linha in linhas:

                # pega da onde vai tal coluna (5-10 ou 0-5)
                for coluna in colunas:

                    # posicionando os barcos horizontalmente
                    if coluna + tamanho <= max(area['colunas']) + 1:

                        posicao_horizontal = [(linha, coluna + index) for index in range(tamanho)]

                        if verificar_posicoes_livres(tamanho_matriz_tabuleiro, posicao_horizontal):
                            posicoes_possiveis_disponiveis.append(posicao_horizontal)

                    # posicionando os barcos verticalmente, pega o tamanho máximo da linha que tem da área, aumenta mais um para verificar se não vai extrapolar
                    if linha + tamanho <= max(area['linhas']) + 1:

                        posicao_vertical = [(linha + index, coluna) for index in range(tamanho)]

                        if verificar_posicoes_livres(tamanho_matriz_tabuleiro, posicao_vertical):

                            posicoes_possiveis_disponiveis.append(posicao_vertical)

            if posicoes_possiveis_disponiveis:

                random.shuffle(posicoes_possiveis_disponiveis)
                posicao_escolhida = posicoes_possiveis_disponiveis[0]
                colocar_navio_tabuleiro(tamanho_matriz_tabuleiro, posicao_escolhida, emojis_navios[nome])


# def escolha_jogador(tamanho_matriz_tabuleiro):



# def escolha_computador(tamanho_matriz_tabuleiro):


def main():

    areas = {
        'area_computador': {'linhas': range(0, 5), 'colunas': range(0, 10)},
        'area_jogador': {'linhas': range(5, 10), 'colunas': range(0, 10)},
    }

    tamanho_matriz_tabuleiro = tabuleiro()
    posicao_tropas(tamanho_matriz_tabuleiro, areas)
    tabuleiro_personalizacao(tamanho_matriz_tabuleiro)
    # escolha_jogador(tamanho_matriz_tabuleiro)
    # escolha_computador(tamanho_matriz_tabuleiro)

main()
# Funções: tabuleiro, posição, verificar posição, colocar posição, fazer jogada (computador e player), verificar jogada