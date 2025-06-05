import re
import shutil
import random

mar = "🌊"

def tabuleiro():

    # Colocando matriz 10x10
    return [[mar for _ in range(10)] for _ in range(10)]

def tabuleiro_personalizacao(tamanho_matriz_tabuleiro):

    # Organizando a matriz, repartindo as áreas do jogador e do computador lado a lado, juntamente com os espaços e as linhas dividindo
    largura_terminal = shutil.get_terminal_size().columns

    area_computador = tamanho_matriz_tabuleiro[:5]   # Linhas 0-4
    area_jogador = tamanho_matriz_tabuleiro[5:]      # Linhas 5-9

    espacos_titulo = max((largura_terminal - 100) // 2, 0)

    print("\n" + " " * espacos_titulo + "\033[1;36mÁREA DO COMPUTADOR\033[0m" + " " * 40 + "\033[1;32mÁREA DO JOGADOR\033[0m\n")

    divisor = ' ' * 20 + '\033[33m║\033[0m' + ' ' * 20

    for linha_cima, linha_baixo in zip(area_computador, area_jogador):

        formatado_cima = ' \033[31m│\033[0m '.join(linha_cima)
        formatado_baixo = ' \033[31m│\033[0m '.join(linha_baixo)

        linha_completa = f"{formatado_cima}{divisor}{formatado_baixo}"
        espacos = max((largura_terminal - len(re.sub(r'\033\[[0-9;]*m', '', linha_completa.strip()))) // 2, 0)
        print(' ' * espacos + linha_completa)

        linha_horizontal = ' \033[36m―\033[0m ' * (len(linha_cima) * 2 - 1)
        linha_horizontal_baixo = ' \033[36m―\033[0m ' * (len(linha_baixo) * 2 - 1)
        linha_horizontal_completa = f"{linha_horizontal}{divisor}{linha_horizontal_baixo}"
        espacos_horizontal = max((largura_terminal - len(re.sub(r'\033\[[0-9;]*m', '', linha_horizontal_completa.strip()))) // 2, 0)
        print(' ' * espacos_horizontal + linha_horizontal_completa)

# Personalização feita pelo chatgpt ^

# Verifica se tem posições livres dentro do loop, caso não tenha, o navio não vai ser colocado naquele lugar, caso contrário, estaá tudo certo
def verificar_posicoes_livres(tamanho_matriz_tabuleiro, posicoes_tropas):

    for linha, coluna in posicoes_tropas:

        if tamanho_matriz_tabuleiro[linha][coluna] != mar:

            return False

    return True

def colocar_navio_tabuleiro(tamanho_matriz_tabuleiro, posicoes_tropas, emoji_navio):

    # Verifica nas linhas e nas colunas, para colocar os emojis 
    for linha, coluna in posicoes_tropas:
        tamanho_matriz_tabuleiro[linha][coluna] = emoji_navio

def configuracoes_tabuleiro(tamanho_matriz_tabuleiro):
    
    # Metade uma área para o usuário e outra metade para o computador
    areas = {

        'area_jogador': {'linhas': range(0, 5), 'colunas': range(0, 10)},
        'area_computador': {'linhas': range(5, 10), 'colunas': range(0, 10)},

    }

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

    escolha_computador(tamanho_matriz_tabuleiro, areas['area_computador'], tamanhos_navios, emojis_navios)
    escolha_jogador(tamanho_matriz_tabuleiro, areas['area_jogador'], tamanhos_navios, emojis_navios)

def escolha_computador(tamanho_matriz_tabuleiro, area, tamanhos_navios, emojis_navios):

    # Coloco os navios em uma lista para poder aletorizar corretamente, ocupando espaço tanto na vertical quanto na horizontal
    navios_lista = list(tamanhos_navios.items())
    random.shuffle(navios_lista)

    # para nome e tamanho na lista de navio, eu verifico cada linha e coluna para que a aletorização não ultrapasse as linhas
    # da matriz
    for nome, tamanho in navios_lista:

        posicoes_possiveis_disponiveis = []

        # coloco as linhas e colunas como lista para poder aleatoriza-las melhor
        linhas = list(area['linhas'])
        colunas = list(area['colunas'])
        random.shuffle(linhas)
        random.shuffle(colunas)

        # Percorrendo todas as linhas e colunas para poder armazenar a posição de cada tropa
        for linha in linhas:

            for coluna in colunas:

                # Configurando posição para horizontalmente
                if coluna + tamanho <= max(area['colunas']) + 1:

                    posicao_horizontal = [(linha, coluna + index) for index in range(tamanho)]

                    # Se for verdadeiro a verificação, vai armazenar as posições na lista
                    if verificar_posicoes_livres(tamanho_matriz_tabuleiro, posicao_horizontal):

                        posicoes_possiveis_disponiveis.append(posicao_horizontal)

                # Configurando posição para verticalmente
                if linha + tamanho <= max(area['linhas']) + 1:

                    posicao_vertical = [(linha + index, coluna) for index in range(tamanho)]

                    # Se for verdadeiro a verificação, vai armazenar as posições na lista
                    if verificar_posicoes_livres(tamanho_matriz_tabuleiro, posicao_vertical):

                        posicoes_possiveis_disponiveis.append(posicao_vertical)

        # Aletorizo agora onde cada posição vai ficar após verificar se vai ser vertical ou horizontal, e então coloco dentro do tabuleiro
        if posicoes_possiveis_disponiveis:

            random.shuffle(posicoes_possiveis_disponiveis)
            posicao_escolhida = posicoes_possiveis_disponiveis[0]
            colocar_navio_tabuleiro(tamanho_matriz_tabuleiro, posicao_escolhida, emojis_navios[nome])

def escolha_jogador(tamanho_matriz_tabuleiro, area, tamanhos_navios, emojis_navios):

    while True:

        for tentativas in range(5):
        
            for linha in range(len(tamanho_matriz_tabuleiro)):

                coordenadas_linha_ataque_jogador = []

                    coordenadas_coluna_ataque_jogador = []

                    posicao_linha_escolha_jogador = int(input(f"Escolha as posições que você deseja atirar! Qual a linha que você deseja atacar? (0-5)"))
                    posicao_coluna_escolha_jogador = int(input(f"Qual a coluna que você deseja atacar?: (5-10)"))

                    linha.append(posicao_linha_escolha_jogador)
                    coluna.append(posicao_coluna_escolha_jogador)



    escolha_computador(tamanho_matriz_tabuleiro, area, tamanhos_navios, emojis_navios)

def main():

    tamanho_matriz_tabuleiro = tabuleiro()
    configuracoes_tabuleiro(tamanho_matriz_tabuleiro)
    tabuleiro_personalizacao(tamanho_matriz_tabuleiro)

main()


# Adaptar o tabuleiro com as linhas sendo de A até J