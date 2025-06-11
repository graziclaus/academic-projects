import re
import shutil
import random

mar = "🌊"

def tabuleiro():

    return [[mar for _ in range(10)] for _ in range(10)]

def tabuleiro_personalizacao(tamanho_matriz_tabuleiro):

    largura_terminal = shutil.get_terminal_size().columns
    area_jogador = tamanho_matriz_tabuleiro[:5]
    area_computador = tamanho_matriz_tabuleiro[5:]
    letras_colunas = [chr(i) for i in range(65, 75)]
    espacos_titulo = max((largura_terminal - 100) // 2, 0)

    print("\n" + " " * espacos_titulo + "\033[1;36mÁREA DO JOGADOR\033[0m" + " " * 60 + "\033[1;32mÁREA DO COMPUTADOR\033[0m\n")
    letras = '    ' + '  '.join([f' {l} ' for l in letras_colunas])
    divisor = '  ' * 10 + '\033[33m║\033[0m' + ' ' * 10
    print(' ' * espacos_titulo + letras + divisor + letras)

    for index, (linha_jogador, linha_computador) in enumerate(zip(area_jogador, area_computador)):
        formatado_jogador = ' \033[31m│\033[0m '.join(linha_jogador)
        tabuleiro_computador_oculto = ['🌊' if celula_tabuleiro != '🌊' else celula_tabuleiro for celula_tabuleiro in linha_computador]
        formatado_computador = ' \033[31m│\033[0m '.join(tabuleiro_computador_oculto)
        linha_completa = f"{index + 1:<2} {formatado_jogador} {divisor} {index + 1:<2} {formatado_computador}"
        espacos = max((largura_terminal - len(re.sub(r'\033\[[0-9;]*m', '', linha_completa.strip()))) // 2, 0)
        print(' ' * espacos + linha_completa)
        linha_horizontal = '\033[36m ―\033[0m' * (len(linha_jogador) * 2 - 1)
        linha_horizontal_computador = '\033[36m ―\033[0m' * (len(linha_computador) * 2 - 1)
        linha_horizontal_completa = f"   {linha_horizontal}{divisor}   {linha_horizontal_computador}"
        espacos_horizontal = max((largura_terminal - len(re.sub(r'\033\[[0-9;]*m', '', linha_horizontal_completa.strip()))) // 2, 0)
        print(' ' * espacos_horizontal + linha_horizontal_completa)

def verificar_posicoes_livres(tamanho_matriz_tabuleiro, posicoes_tropas):

    for linha, coluna in posicoes_tropas:

        if tamanho_matriz_tabuleiro[linha][coluna] != mar:

            return False

    return True

def colocar_navio_tabuleiro(tamanho_matriz_tabuleiro, posicoes_tropas, emoji_navio):

    for linha, coluna in posicoes_tropas:

        tamanho_matriz_tabuleiro[linha][coluna] = emoji_navio

def configuracoes_tabuleiro(tamanho_matriz_tabuleiro):

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

    navios_lista = list(tamanhos_navios.items())
    random.shuffle(navios_lista)

    for nome, tamanho in navios_lista:

        posicoes_possiveis_disponiveis = []
        linhas = list(area['linhas'])
        colunas = list(area['colunas'])
        random.shuffle(linhas)
        random.shuffle(colunas)

        for linha in linhas:

            for coluna in colunas:

                if coluna + tamanho <= max(area['colunas']) + 1:

                    posicao_horizontal = [(linha, coluna + index) for index in range(tamanho)]

                    if verificar_posicoes_livres(tamanho_matriz_tabuleiro, posicao_horizontal):

                        posicoes_possiveis_disponiveis.append(posicao_horizontal)

                if linha + tamanho <= max(area['linhas']) + 1:

                    posicao_vertical = [(linha + index, coluna) for index in range(tamanho)]

                    if verificar_posicoes_livres(tamanho_matriz_tabuleiro, posicao_vertical):

                        posicoes_possiveis_disponiveis.append(posicao_vertical)

        if posicoes_possiveis_disponiveis:

            random.shuffle(posicoes_possiveis_disponiveis)
            posicao_escolhida = posicoes_possiveis_disponiveis[0]
            colocar_navio_tabuleiro(tamanho_matriz_tabuleiro, posicao_escolhida, "🐙")

def escolha_jogador(tamanho_matriz_tabuleiro, area, tamanhos_navios, emojis_navios):

    navios_lista = list(tamanhos_navios.items())

    for nome, tamanho in navios_lista:

        while True:

            print(f"\nVamos posicionar seu navio: \033[1m{nome.upper()}\033[0m, esse navio tem o tamanho de ({tamanho} espaços)")
            tabuleiro_personalizacao(tamanho_matriz_tabuleiro)

            posicao_linha_escolha_jogador = int(input(f"Escolha as posições que você deseja colocar seus navios! Qual a linha inicial que você quer posicionar? (1-5): "))
            posicao_coluna_escolha_jogador = input(f"Qual a coluna inicial que você quer posicionar? (A-J):").upper()
            direcao_navio = input("Qual direção você deseja colocar seu navio? (Horizontal ou Vertical): ").lower()

            if not (1 <= posicao_linha_escolha_jogador <= 5):

                print("A linha precisa ser um número entre 1 e 5! Tente novamente.")
                continue

            posicao_linha_escolha_jogador -= 1

            if posicao_coluna_escolha_jogador not in "ABCDEFGHIJ":

                print("Coluna inválida! Digite uma letra de A até J.")
                continue

            posicao_coluna_escolha_jogador = ord(posicao_coluna_escolha_jogador) - ord('A')

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

            if not verificar_posicoes_livres(tamanho_matriz_tabuleiro, posicoes):

                print("Já tem navio nessa posição. Escolha outra.")
                continue

            print("\n\033[1mSeu tabuleiro agora:\033[0m")
            tabuleiro_personalizacao(tamanho_matriz_tabuleiro)
            colocar_navio_tabuleiro(tamanho_matriz_tabuleiro, posicoes, emojis_navios[nome])
            print(f"Navio {nome} posicionado!\n")
            break

# Minha parte ^

def ataque_jogador(tamanho_matriz_tabuleiro, tabuleiro_acertos_erros):

    while True:

        linha = int(input("Digite a linha para atacar (6-10): "))
        coluna = input("Digite a coluna para atacar (A-J): ").upper()

        if linha < 6 or linha > 10:

            print("Linha inválida! Só pode atacar da linha 6 até a 10.")
            continue

        if coluna not in "ABCDEFGHIJ":

            print("Coluna inválida! Use A até J.")
            continue

        linha -= 1
        coluna = ord(coluna) - ord('A')

        if tabuleiro_acertos_erros[linha][coluna] != mar:
            print("Você já atacou essa posição, tente outra.")
            continue

        if tamanho_matriz_tabuleiro[linha][coluna] == mar:

            print("Água! Você errou.")
            tabuleiro_acertos_erros[linha][coluna] = '❌'
            return False

        else:

            print("Acertou um navio! Você pode atacar de novo.")
            tabuleiro_acertos_erros[linha][coluna] = '💥'
            return True

def ataque_computador(tamanho_matriz_tabuleiro, tabuleiro_acertos_erros):

    while True:

        linha = random.randint(5, 9)
        coluna = random.randint(0, 9)

        if tabuleiro_acertos_erros[linha][coluna] == mar:

            if tamanho_matriz_tabuleiro[linha][coluna] == mar:

                print(f"Computador atacou {linha+1}{chr(coluna + ord('A'))} e errou!")
                tabuleiro_acertos_erros[linha][coluna] = '❌'
                return False

            else:

                print(f"Computador atacou {linha+1}{chr(coluna + ord('A'))} e acertou um navio! Vai jogar de novo.")
                tabuleiro_acertos_erros[linha][coluna] = '💥'
                return True

def mostrar_tabuleiro_jogo(tamanho_matriz_tabuleiro, tabuleiro_acertos_erros):

    largura_terminal = shutil.get_terminal_size().columns

    area_jogador = tamanho_matriz_tabuleiro[:5]
    area_computador = tamanho_matriz_tabuleiro[5:]

    acertos_erros_area_computador = tabuleiro_acertos_erros[5:]

    letras_colunas = [chr(i) for i in range(65, 75)]  # A-J
    espacos_titulo = max((largura_terminal - 50) // 2, 0)

    print("\n" + " " * espacos_titulo + "\033[1;32mÁREA DO COMPUTADOR - ATAQUES\033[0m\n")

    letras = '    ' + '  '.join([f' {l} ' for l in letras_colunas])
    print(' ' * espacos_titulo + letras)

    for index, (linha_computador, linha_ataques) in enumerate(zip(area_computador, acertos_erros_area_computador)):
        linha_mostrada = []

        for i, celula in enumerate(linha_computador):

            if linha_ataques[i] == '💥':

                linha_mostrada.append('💥')

            elif linha_ataques[i] == '❌':

                linha_mostrada.append('❌')

            else:

                linha_mostrada.append('🌊')

        print(f"{index + 6:<2} " + ' │ '.join(linha_mostrada))

def mostrar_tabuleiros_final(tamanho_matriz_tabuleiro):

    largura_terminal = shutil.get_terminal_size().columns
    area_jogador = tamanho_matriz_tabuleiro[:5]
    area_computador = tamanho_matriz_tabuleiro[5:]
    letras_colunas = [chr(i) for i in range(65, 75)]
    espacos_titulo = max((largura_terminal - 100) // 2, 0)

    print("\n" + " " * espacos_titulo + "\033[1;36mÁREA DO JOGADOR\033[0m" + " " * 60 + "\033[1;32mÁREA DO COMPUTADOR\033[0m\n")
    letras = '    ' + '  '.join([f' {l} ' for l in letras_colunas])
    divisor = '  ' * 10 + '\033[33m║\033[0m' + ' ' * 10
    print(' ' * espacos_titulo + letras + divisor + letras)

    for index, (linha_jogador, linha_computador) in enumerate(zip(area_jogador, area_computador)):

        formatado_jogador = ' \033[31m│\033[0m '.join(linha_jogador)
        formatado_computador = ' \033[31m│\033[0m '.join(linha_computador)
        linha_completa = f"{index + 1:<2} {formatado_jogador} {divisor} {index + 6:<2} {formatado_computador}"
        espacos = max((largura_terminal - len(re.sub(r'\033\[[0-9;]*m', '', linha_completa.strip()))) // 2, 0)
        print(' ' * espacos + linha_completa)
        linha_horizontal = '\033[36m ―\033[0m' * (len(linha_jogador) * 2 - 1)
        linha_horizontal_computador = '\033[36m ―\033[0m' * (len(linha_computador) * 2 - 1)
        linha_horizontal_completa = f"   {linha_horizontal}{divisor}   {linha_horizontal_computador}"
        espacos_horizontal = max((largura_terminal - len(re.sub(r'\033\[[0-9;]*m', '', linha_horizontal_completa.strip()))) // 2, 0)
        print(' ' * espacos_horizontal + linha_horizontal_completa)

def verificar_fim_jogo(tamanho_matriz_tabuleiro, tabuleiro_acertos_erros):

    for linha in range(5, 10):

        for coluna in range(10):

            if tamanho_matriz_tabuleiro[linha][coluna] != mar and tabuleiro_acertos_erros[linha][coluna] != '💥':

                return False

    return True

def jogo_batalha_naval(tamanho_matriz_tabuleiro):

    tabuleiro_acertos_erros = [[mar for _ in range(10)] for _ in range(10)]
    turno_jogador = True

    print("\nVamos começar o jogo! Você vai atacar a área do computador (linhas 6 a 10).")

    while True:
        tabuleiro_personalizacao(tamanho_matriz_tabuleiro)
        mostrar_tabuleiro_jogo(tamanho_matriz_tabuleiro, tabuleiro_acertos_erros)

        if turno_jogador:
            print("\n\033[1;34mSua vez de atacar!\033[0m")
            acertou = ataque_jogador(tamanho_matriz_tabuleiro, tabuleiro_acertos_erros)
        else:
            print("\n\033[1;31mVez do computador atacar!\033[0m")
            acertou = ataque_computador(tamanho_matriz_tabuleiro, tabuleiro_acertos_erros)

        if not acertou:
            turno_jogador = not turno_jogador

        if verificar_fim_jogo(tamanho_matriz_tabuleiro, tabuleiro_acertos_erros):
            if turno_jogador:
                print("\n\033[1;32mParabéns! Você venceu a batalha!\033[0m")
            else:
                print("\n\033[1;31mO computador venceu a batalha!\033[0m")

            mostrar_tabuleiros_final(tamanho_matriz_tabuleiro)
            break

        input("\nPressione Enter para continuar...")

def main():

    tamanho_matriz_tabuleiro = tabuleiro()
    configuracoes_tabuleiro(tamanho_matriz_tabuleiro)
    tabuleiro_personalizacao(tamanho_matriz_tabuleiro)

    jogo_batalha_naval(tamanho_matriz_tabuleiro)

if __name__ == "__main__":
    main()