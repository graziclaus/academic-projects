import re
import shutil
import random

mar = "🌊"


def criar_tabuleiro():

    return [[mar for _ in range(10)] for _ in range(5)]

def verificar_posicoes_livres(tabuleiro, posicoes):

    for linha, coluna in posicoes:

        if not (0 <= linha < 5 and 0 <= coluna < 10):

            return False

        if tabuleiro[linha][coluna] != mar:

            return False

    return True


def colocar_navio(tabuleiro, posicoes, emoji):

    for linha, coluna in posicoes:

        tabuleiro[linha][coluna] = emoji


def print_tabuleiros_inicial_e_final(tabuleiro_jogador, tabuleiro_computador, is_final=False):

    largura_terminal = shutil.get_terminal_size().columns
    letras_colunas = [chr(i) for i in range(65, 75)]
    espacos_titulo = max((largura_terminal - 100) // 2, 0)

    print(
        "\n" + " " * espacos_titulo + "\033[1;36mSEU TABULEIRO\033[0m" + " " * 60 + "\033[1;32mTABULEIRO DO COMPUTADOR\033[0m\n")
    letras = '    ' + '  '.join([f' {l} ' for l in letras_colunas])
    divisor = '  ' * 10 + '\033[33m║\033[0m' + ' ' * 10
    print(' ' * espacos_titulo + letras + divisor + letras)

    for index in range(5):

        formatado_jogador = ' \033[31m│\033[0m '.join(tabuleiro_jogador[index])

        if not is_final:

            tabuleiro_computador_oculto = ['🌊' if celula_tabuleiro not in ['💥', '❌'] else celula_tabuleiro for celula_tabuleiro in tabuleiro_computador[index]]
            formatado_computador = ' \033[31m│\033[0m '.join(tabuleiro_computador_oculto)

        else:

            formatado_computador = ' \033[31m│\033[0m '.join(tabuleiro_computador[index])

        linha_completa = f"{index + 1:<2} {formatado_jogador} {divisor} {index + 1:<2} {formatado_computador}"
        espacos = max((largura_terminal - len(re.sub(r'\033\[[0-9;]*m', '', linha_completa.strip()))) // 2, 0)
        print(' ' * espacos + linha_completa)

        if index < 4:

            linha_horizontal = '\033[36m ―\033[0m' * (len(tabuleiro_jogador[index]) * 2 - 1)
            linha_horizontal_completa = f"   {linha_horizontal}{divisor}   {linha_horizontal}"
            espacos_horizontal = max((largura_terminal - len(re.sub(r'\033\[[0-9;]*m', '', linha_horizontal_completa.strip()))) // 2, 0)
            print(' ' * espacos_horizontal + linha_horizontal_completa)

def escolha_jogador(tabuleiro_oculto_jogador, tamanhos_navios, emojis_navios, navios_jogador):

    for nome, tamanho in tamanhos_navios.items():

        while True:

            print(f"\nPosicione seu navio: \033[1m{nome.upper()}\033[0m ({tamanho} espaços)")

            print("\n\033[1;36mSeu Tabuleiro:\033[0m")

            for i, linha in enumerate(tabuleiro_oculto_jogador):

                print(f"{i + 1:<2} " + ' │ '.join(linha))

            print('    ' + '  '.join([f' {chr(i)} ' for i in range(65, 75)]))

            entrada_linha = input("Linha inicial (1-5): ")
            coluna_str = input("Coluna inicial (A-J): ").upper()
            direcao = input("Direção (Horizontal/Vertical): ").lower()

            if not entrada_linha.isdigit():

                print("Linha inválida. Digite um número entre 1 e 5.")
                continue

            linha = int(entrada_linha) - 1

            if not (0 <= linha < 5):

                print("Linha inválida. Digite um número entre 1 e 5.")
                continue

            if coluna_str not in "ABCDEFGHIJ":

                print("Coluna inválida. Digite uma letra de A até J.")
                continue

            coluna = ord(coluna_str) - ord('A')

            if direcao not in ["horizontal", "vertical"]:

                print("Direção inválida. Use 'Horizontal' ou 'Vertical'.")
                continue

            if direcao == "horizontal":

                if coluna + tamanho > 10:

                    print("Navio não cabe horizontalmente nessa posição. Tente outra.")
                    continue

                posicoes = [(linha, coluna + i) for i in range(tamanho)]

            else:

                if linha + tamanho > 5:

                    print("Navio não cabe verticalmente nessa posição. Tente outra.")
                    continue

                posicoes = [(linha + i, coluna) for i in range(tamanho)]

            if not verificar_posicoes_livres(tabuleiro_oculto_jogador, posicoes):

                print("Já tem navio nessa posição. Escolha outra.")
                continue

            colocar_navio(tabuleiro_oculto_jogador, posicoes, emojis_navios[nome])

            navios_jogador.append({'nome': nome, 'tamanho': tamanho, 'emoji': emojis_navios[nome], 'posicoes_restantes': posicoes.copy()})

            print(f"Navio {nome} posicionado!\n")
            print("\n\033[1mSeu tabuleiro agora:\033[0m")

            for i, linha_tab in enumerate(tabuleiro_oculto_jogador):

                print(f"{i + 1:<2} " + ' │ '.join(linha_tab))

            print('    ' + '  '.join([f' {chr(i)} ' for i in range(65, 75)]))
            break


def escolha_computador(tabuleiro_oculto_computador, tamanhos_navios, emojis_navios, navios_computador):

    navios_lista = list(tamanhos_navios.items())
    random.shuffle(navios_lista)

    for nome, tamanho in navios_lista:

        while True:

            direcao = random.choice(["horizontal", "vertical"])
            linha = random.randint(0, 4)
            coluna = random.randint(0, 9)

            if direcao == "horizontal":

                if coluna + tamanho > 10:
                    continue

                posicoes = [(linha, coluna + i) for i in range(tamanho)]

            else:

                if linha + tamanho > 5:

                    continue

                posicoes = [(linha + i, coluna) for i in range(tamanho)]

            if verificar_posicoes_livres(tabuleiro_oculto_computador, posicoes):

                colocar_navio(tabuleiro_oculto_computador, posicoes, emojis_navios[nome])

                navios_computador.append({'nome': nome, 'tamanho': tamanho, 'emoji': emojis_navios[nome],'posicoes_restantes': posicoes.copy()})
                break

# ------------------------------------------------------ \\ ---------------------------------------------- \\ ------------------------------------------------------------

def ataque(tabuleiro_oculto, tabuleiro_visivel, is_jogador, navios_alvo):

    while True:
        if is_jogador:
            try:
                linha = int(input("Atacar linha (1-5): ")) - 1
            except ValueError:
                print("Linha inválida.")
                continue
            coluna_str = input("Atacar coluna (A-J): ").upper()
            if not (0 <= linha < 5) or coluna_str not in "ABCDEFGHIJ":
                print("Entrada inválida.")
                continue
            coluna = ord(coluna_str) - ord('A')
        else:
            linha = random.randint(0, 4)
            coluna = random.randint(0, 9)

        if not (0 <= linha < 5 and 0 <= coluna < 10):
            if is_jogador:
                print("Posição fora dos limites do tabuleiro. Tente novamente.")
            continue

        if tabuleiro_visivel[linha][coluna] != mar:
            if is_jogador:
                print("Você já atacou essa posição. Tente outra.")
            continue

        if tabuleiro_oculto[linha][coluna] != mar:
            tabuleiro_visivel[linha][coluna] = '💥'
            posicao_atingida = (linha, coluna)

            for navio in navios_alvo:
                if posicao_atingida in navio['posicoes_restantes']:
                    navio['posicoes_restantes'].remove(posicao_atingida)
                    if not navio['posicoes_restantes']:
                        if is_jogador:
                            print(f"\033[1;32mVocê afundou o {navio['nome'].upper()} do computador!\033[0m")
                        else:
                            print(f"\033[1;31mO computador afundou seu {navio['nome'].upper()}!\033[0m")
                    break

            if is_jogador:
                print("Acertou um navio! Você pode atacar de novo.")
            else:
                print(f"Computador atacou {linha + 1}{chr(coluna + 65)} e acertou um navio! Vai jogar de novo.")
            return True
        else:
            tabuleiro_visivel[linha][coluna] = '❌'
            if is_jogador:
                print("Água! Você errou.")
            else:
                print(f"Computador atacou {linha + 1}{chr(coluna + 65)} e errou.")
            return False


def fim_jogo(navios):

    for navio in navios:
        if navio['posicoes_restantes']:
            return False
    return True


def contar_navios_restantes(navios):

    return sum(1 for navio in navios if navio['posicoes_restantes'])


def print_tabuleiros_jogo(tabuleiro_oculto_jogador, tabuleiro_visivel_computador, tabuleiro_visivel_jogador, navios_jogador, navios_computador):

    largura_terminal = shutil.get_terminal_size().columns
    letras_colunas = [chr(i) for i in range(65, 75)]  # A-J
    espacos_titulo = max((largura_terminal - 100) // 2, 0)

    print(
        "\n" + " " * espacos_titulo + "\033[1;32mSEUS ATAQUES (COMPUTADOR)\033[0m" + " " * 60 + "\033[1;36mSEU TABULEIRO (ATAQUES DO COMPUTADOR)\033[0m\n")
    letras = '    ' + '  '.join([f' {l} ' for l in letras_colunas])
    divisor = '  ' * 10 + '\033[33m║\033[0m' + ' ' * 10
    print(' ' * espacos_titulo + letras + divisor + letras)

    for index in range(5):

        linha_jogador_ve_computador = ' \033[31m│\033[0m '.join(tabuleiro_visivel_computador[index])


        linha_do_jogador = []
        for coluna in range(10):
            if tabuleiro_visivel_jogador[index][coluna] != mar:
                linha_do_jogador.append(tabuleiro_visivel_jogador[index][coluna])
            else:
                linha_do_jogador.append(tabuleiro_oculto_jogador[index][coluna])
        formatado_meu_tabuleiro = ' \033[31m│\033[0m '.join(linha_do_jogador)

        linha_completa = f"{index + 1:<2} {linha_jogador_ve_computador} {divisor} {index + 1:<2} {formatado_meu_tabuleiro}"
        espacos = max((largura_terminal - len(re.sub(r'\033\[[0-9;]*m', '', linha_completa.strip()))) // 2, 0)
        print(' ' * espacos + linha_completa)

        if index < 4:
            linha_horizontal = '\033[36m ―\033[0m' * (len(tabuleiro_visivel_computador[index]) * 2 - 1)
            linha_horizontal_completa = f"   {linha_horizontal}{divisor}   {linha_horizontal}"
            espacos_horizontal = max(
                (largura_terminal - len(re.sub(r'\033\[[0-9;]*m', '', linha_horizontal_completa.strip()))) // 2, 0)
            print(' ' * espacos_horizontal + linha_horizontal_completa)


    navios_restantes_jogador = contar_navios_restantes(navios_jogador)
    navios_restantes_computador = contar_navios_restantes(navios_computador)
    print(
        f"\n\033[1mNavios restantes:\033[0m Seu: {navios_restantes_jogador} | Computador: {navios_restantes_computador}")


def jogo_batalha_naval(tabuleiro_oculto_jogador, tabuleiro_visivel_jogador, tabuleiro_oculto_computador, tabuleiro_visivel_computador, navios_jogador, navios_computador):

    turno_jogador = True

    print("\nVamos começar o jogo! Você vai atacar o tabuleiro do computador e o computador vai atacar o seu.")

    while True:

        print_tabuleiros_jogo(tabuleiro_oculto_jogador, tabuleiro_visivel_computador, tabuleiro_visivel_jogador,
                              navios_jogador, navios_computador)

        if turno_jogador:
            print("\n\033[1;34mSua vez de atacar!\033[0m")

            acertou = ataque(tabuleiro_oculto_computador, tabuleiro_visivel_computador, True, navios_computador)
            if fim_jogo(navios_computador):
                print("\n\033[1;32mParabéns! Você venceu a batalha!\033[0m")
                print_tabuleiros_inicial_e_final(tabuleiro_oculto_jogador, tabuleiro_oculto_computador, is_final=True)
                break
        else:
            print("\n\033[1;31mVez do computador atacar!\033[0m")

            acertou = ataque(tabuleiro_oculto_jogador, tabuleiro_visivel_jogador, False, navios_jogador)
            if fim_jogo(navios_jogador):
                print("\n\033[1;31mO computador venceu a batalha!\033[0m")
                print_tabuleiros_inicial_e_final(tabuleiro_oculto_jogador, tabuleiro_oculto_computador, is_final=True)
                break

        if not acertou:
            turno_jogador = not turno_jogador


def main():

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

    tabuleiro_oculto_jogador = criar_tabuleiro()
    tabuleiro_visivel_jogador = criar_tabuleiro()
    tabuleiro_oculto_computador = criar_tabuleiro()
    tabuleiro_visivel_computador = criar_tabuleiro()


    navios_jogador = []
    navios_computador = []


    escolha_computador(tabuleiro_oculto_computador, tamanhos_navios, emojis_navios, navios_computador)
    escolha_jogador(tabuleiro_oculto_jogador, tamanhos_navios, emojis_navios, navios_jogador)


    print_tabuleiros_inicial_e_final(tabuleiro_oculto_jogador, tabuleiro_oculto_computador, is_final=False)
    input("\nNavios posicionados! Pressione Enter para iniciar o jogo...")

    jogo_batalha_naval(tabuleiro_oculto_jogador, tabuleiro_visivel_jogador, tabuleiro_oculto_computador,
                       tabuleiro_visivel_computador, navios_jogador, navios_computador)


if __name__ == "__main__":
    main()
