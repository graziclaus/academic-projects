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

    # Pegando as 5 primeiras linhas da matriz (linhas 0 a 4) pro jogador e as 5 últimas (5 a 9) pro computador
    area_jogador = tamanho_matriz_tabuleiro[:5]  # Linhas para o jogador: 0-4
    area_computador = tamanho_matriz_tabuleiro[5:]  # Linhas para o computador: 5-9

    # Colocando as colunas em letras. A função chr(i) converte um número (código ASCII) para o caractere correspondente. Os valores 65 até 74 correspondem às letras maiúsculas de A até J:
    letras_colunas = [chr(i) for i in range(65, 75)]  # A–J
    # Espaços entre os títulos "ÁREA DO JOGADOR" e "ÁREA DO COMPUTADOR"
    espacos_titulo = max((largura_terminal - 100) // 2, 0)

    print(
        "\n" + " " * espacos_titulo + "\033[1;36mÁREA DO JOGADOR\033[0m" + " " * 40 + "\033[1;32mÁREA DO COMPUTADOR\033[0m\n")

    # Formatando as letras A–J com espaçamento entre elas para exibição nas colunas
    letras = '    ' + '  '.join([f' {l} ' for l in letras_colunas])


    # Espaço entre os dois tabuleiros
    divisor = '  ' * 10 + '\033[33m║\033[0m' + ' ' * 10
    print(' ' * espacos_titulo + letras + divisor + letras)

    # Personalização para as áreas do jogador e computador
    for index, (linha_jogador, linha_computador) in enumerate(zip(area_jogador, area_computador)):

        # Tabuleiro do jogador
        formatado_jogador = ' \033[31m│\033[0m '.join(linha_jogador)

        # Ocultando a área do computador
        tabuleiro_computador_oculto = ['🌊' if celula_tabuleiro != '🌊' else celula_tabuleiro for celula_tabuleiro in linha_computador]
        formatado_computador = ' \033[31m│\033[0m '.join(tabuleiro_computador_oculto)

        # Para deixar visível:
        # formatado_computador = ' \033[31m│\033[0m '.join(linha_computador)

        # Colocando os números 1 ao 10
        linha_completa = f"{index + 1:<2} {formatado_jogador} {divisor} {index + 1:<2} {formatado_computador}"
        espacos = max((largura_terminal - len(re.sub(r'\033\[[0-9;]*m', '', linha_completa.strip()))) // 2, 0)
        print(' ' * espacos + linha_completa)

        # Adicionando linhas horizontais azuis entre cada linha do tabuleiro para visualização
        linha_horizontal = '\033[36m ―\033[0m' * (len(linha_jogador) * 2 - 1)
        linha_horizontal_computador = '\033[36m ―\033[0m' * (len(linha_computador) * 2 - 1)
        linha_horizontal_completa = f"   {linha_horizontal}{divisor}   {linha_horizontal_computador}"

        espacos_horizontal = max(
            (largura_terminal - len(re.sub(r'\033\[[0-9;]*m', '', linha_horizontal_completa.strip()))) // 2, 0)
        print(' ' * espacos_horizontal + linha_horizontal_completa)

# Personalização feita pelo chatgpt com alguns ajustes meus ^

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

    # Para cada navio, verifica as posições possíveis sem ultrapassar os limites da matriz
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
            tabuleiro_personalizacao(tamanho_matriz_tabuleiro)

            posicao_linha_escolha_jogador = int(input(f"Escolha as posições que você deseja colocar seus navios?! Qual a linha inicial que você quer posicionar? (1-5): "))
            posicao_coluna_escolha_jogador = input(f"Qual a coluna inicial que você quer posicionar? (A-J):").upper()
            direcao_navio = input("Qual direção você deseja colocar seu navio? (Horizontal ou Vertical): ").lower()

            # Verificações da linha, caso o usuário coloque algo errado. Ajusta também o número para o usuário, pois 0-4 seria estranho, normalmente é 1-5
            if not (1 <= posicao_linha_escolha_jogador <= 5):

                print("A linha precisa ser um número entre 1 e 5! Tente novamente.")

                continue

            posicao_linha_escolha_jogador -= 1

            if posicao_linha_escolha_jogador not in area['linhas']:

                print("Linha fora da sua área! Tente entre 1 e 5.")
                continue

            # Verificação da coluna se está entre A até J. Também converte as letras em números (A=0, B=1, ..., J=9)
            if posicao_coluna_escolha_jogador not in "ABCDEFGHIJ":
                print("Coluna inválida! Digite uma letra de A até J.")
                continue

            posicao_coluna_escolha_jogador = ord(posicao_coluna_escolha_jogador) - ord('A')

            # Verificação da direção do navio, só pode horizontal e vertical, diagonal não.
            if direcao_navio not in ["horizontal", "vertical"]:

                print("Direção inválida! Use 'Horizontal' ou 'Vertical'.")

                continue

            if direcao_navio == "horizontal":

                if posicao_coluna_escolha_jogador + tamanho > max(area['colunas']) + 1:

                    print("Navio não cabe horizontalmente nessa posição! Tente outra.")
                    continue

                posicoes = [(posicao_linha_escolha_jogador, posicao_coluna_escolha_jogador + index) for index in range(tamanho)]

            else:

                if posicao_linha_escolha_jogador + tamanho > max(area['linhas']) + 1:

                    print("Navio não cabe verticalmente nessa posição. Tente outra.")
                    continue

                posicoes = [(posicao_linha_escolha_jogador + index, posicao_coluna_escolha_jogador) for index in range(tamanho)]

            # Verifica se tem espaços
            if not verificar_posicoes_livres(tamanho_matriz_tabuleiro, posicoes):

                print("Já tem navio nessa posição. Escolha outra.")
                continue

            # Display do tabuleiro para cada vez que colocar o navio
            print("\n\033[1mSeu tabuleiro agora:\033[0m")
            tabuleiro_personalizacao(tamanho_matriz_tabuleiro)
            colocar_navio_tabuleiro(tamanho_matriz_tabuleiro, posicoes, emojis_navios[nome])
            print(f"Navio {nome} posicionado!\n")
            break

def main():

    tamanho_matriz_tabuleiro = tabuleiro()
    configuracoes_tabuleiro(tamanho_matriz_tabuleiro)
    tabuleiro_personalizacao(tamanho_matriz_tabuleiro)

main()

# OBJETIVOS

# Criar e inicializar os tabuleiros (10x10) ✅
# Tabuleiro oculto e visível ✅
# Função posicionar navio (computador e jogador com validações) ✅


# 1. O programa deve respeitar as regras do jogo que foram especificadas na Introdução. (2,0)
# 2. O jogo deve funcionar corretamente do início ao fim (sem bugs), seguindo o fluxo especificado na
# Introdução. (3,0)
# 3. O código deve estar modulado em funções. (1,5)
# 4. Os tabuleiros devem utilizar matrizes. (1,5)
# 5. Feedback correto ao jogador. (2,0)
# 6. Desafio (nota extra): Implementar o jogo batalha naval original, de forma que possua todas as
# embarcações, sendo elas: Porta-aviões (ocupando 5 posições), Navio-tanque (ocupando 4
# posições), Contratorpedeiro (ocupando 3 posições), Submarino (ocupando duas posições) e
# Destroier (ocupando 1 posição). Neste modo a embarcação só afunda quando todas as posições
# dela tiverem sido atingidas. Quando uma embarcação tiver todas as suas partes atingidas, a
# embarcação é então afundada e o jogador pode atacar novamente. (1,0)
