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

    navios_lista = list(tamanhos_navios.items())

    for nome, tamanho in navios_lista:

        while True:

            print(f"\nVamos posicionar seu navio: \033[1m{nome.upper()}\033[0m, esse navio tem o tamanho de ({tamanho} espaços)")

            posicao_linha_escolha_jogador = int(input(f"Escolha as posições que você deseja colocar seus navios?! Qual a linha inicial que você quer posicionar? (0-5)"))
            posicao_coluna_escolha_jogador = int(input(f"Qual a coluna inicial que você quer posicionar?: (5-10)"))
            direcao_navio = input("Qual direção você deseja colocar seu navio? (Horizontal ou Vertical): ").lower()

            if not (0 <= posicao_linha_escolha_jogador <= 5 <= posicao_coluna_escolha_jogador <= 10):

                print("Você colocou algum digito errado ou a linha/coluna não é da sua área! Tente novamente.")

                continue

            if direcao_navio not in ["horizontal", "vertical"]:

                print("Direção inválida! Use 'Horizontal' ou 'Vertical'.")

                continue

            if direcao_navio == "horizontal":

                if posicao_linha_escolha_jogador + tamanho <= max(area['colunas']) + 1:

                    print("Navio não cabe horizontalmente nessa posição! Tente outra.")
                    continue

                posicoes = [(posicao_linha_escolha_jogador, posicao_coluna_escolha_jogador + index) for index in range(tamanho)]

            else:

                if posicao_linha_escolha_jogador + tamanho > max(area['linhas']) + 1:

                    print("Navio não cabe verticalmente nessa posição. Tente outra.")
                    continue

                posicoes = [(posicao_linha_escolha_jogador + index, posicao_coluna_escolha_jogador) for index in range(tamanho)]

            if not verificar_posicoes_livres(tamanho_matriz_tabuleiro, posicoes):

                print("Já tem navio nessa posição. Escolha outra.")
                continue

            print("\n\033[1mSeu tabuleiro agora:\033[0m")
            tabuleiro_personalizacao(tamanho_matriz_tabuleiro)
            colocar_navio_tabuleiro(tamanho_matriz_tabuleiro, posicoes, emojis_navios[nome])
            print(f"Navio {nome} posicionado!\n")
            break

            # fiz alguma coisa nas linhas e colunas, a distribuição de linhas e colunas devem estar erradas

def main():

    tamanho_matriz_tabuleiro = tabuleiro()
    configuracoes_tabuleiro(tamanho_matriz_tabuleiro)
    tabuleiro_personalizacao(tamanho_matriz_tabuleiro)

main()


# Adaptar o tabuleiro com as linhas sendo de A até J