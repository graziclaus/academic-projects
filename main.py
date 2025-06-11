# instalação via terminal -> pip install pillow rich #
import re
import shutil
import random
from time import sleep
import time
from PIL import Image, ImageDraw
from rich.console import Console

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
        "\n" + " " * espacos_titulo + "\033[1;36mSEU TABULEIRO\033[0m" + " " * 60 + "\033[1;32mTABULEIRO DOS ALIENÍGENAS\033[0m\n")
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

                colocar_navio(tabuleiro_oculto_computador, posicoes, "🐙") # Usa sempre o polvo

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
                            print(f"\033[1;32mVocê afundou o {navio['nome'].upper()} dos alienígenas!\033[0m")
                        else:
                            print(f"\033[1;31mOs alienígenas afundaram seu {navio['nome'].upper()}!\033[0m")
                    break

            if is_jogador:
                print("Acertou um navio! Você pode atacar de novo.")
            else:
                print(f"Alienígenas atacaram {linha + 1}{chr(coluna + 65)} e acertaram um navio! Vão jogar de novo.")
            return True
        else:
            tabuleiro_visivel[linha][coluna] = '❌'
            if is_jogador:
                print("Água! Você errou.")
            else:
                print(f"Alienígenas atacaram {linha + 1}{chr(coluna + 65)} e erraram.")
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
        "\n" + " " * espacos_titulo + "\033[1;32mSEUS ATAQUES (ALIENÍGENAS)\033[0m" + " " * 60 + "\033[1;36mSEU TABULEIRO (ATAQUES DOS ALIENÍGENAS)\033[0m\n")
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
        f"\n\033[1mNavios restantes:\033[0m Seu: {navios_restantes_jogador} | Alienígenas: {navios_restantes_computador}")


def jogo_batalha_naval(tabuleiro_oculto_jogador, tabuleiro_visivel_jogador, tabuleiro_oculto_computador, tabuleiro_visivel_computador, navios_jogador, navios_computador):

    turno_jogador = True

     print("\nVamos começar o jogo! Você vai atacar o tabuleiro dos alienígenas e os alienígenas vão atacar o seu.")

    while True:

        print_tabuleiros_jogo(tabuleiro_oculto_jogador, tabuleiro_visivel_computador, tabuleiro_visivel_jogador,
                              navios_jogador, navios_computador)

        if turno_jogador:
            print("\n\033[1;34mSua vez de atacar!\033[0m")

            acertou = ataque(tabuleiro_oculto_computador, tabuleiro_visivel_computador, True, navios_computador)
             pixel_artWIN()
                print("\n\033[1;32mParabéns! Você venceu a batalha contra os alienígenas!\033[0m")
                print_tabuleiros_inicial_e_final(tabuleiro_oculto_jogador, tabuleiro_oculto_computador, is_final=True)
                break
        else:
            print("\n\033[1;31mVez do computador atacar!\033[0m")

            acertou = ataque(tabuleiro_oculto_jogador, tabuleiro_visivel_jogador, False, navios_jogador)
            if fim_jogo(navios_jogador):
                pixel_artLOST
                print("\n\033[1;31mO Você perdeu! As tropas alienigenas conseguiram reguperar o pequeno alienígena.\033[0m")
                print_tabuleiros_inicial_e_final(tabuleiro_oculto_jogador, tabuleiro_oculto_computador, is_final=True)
                break

        if not acertou:
            turno_jogador = not turno_jogador
        if not turno_jogador:
            time.sleep(3)


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


    
def digitar_com_pausa(texto, pausa_entre_caracteres=0.05, pausa_nos_pontos=0.5, linhas=0.00):
  for caractere in texto:
    print(caractere, end="", flush=True)
    time.sleep(pausa_entre_caracteres)
    if caractere == ".":
      time.sleep(pausa_nos_pontos)
    elif caractere == "!":
      time.sleep(pausa_nos_pontos)
    elif caractere == "-":
        time.sleep(linhas)
  print()

def inicio_de_batalha():
    pixel_artSTART()
    print("Prepare-se para batalha!")
    if __name__ == "__main__":

        main()

def pixel_artPOLVO():
    console = Console()

    def criar_pixel_art(path="polvo.png"):
        largura = 30
        altura = 10
        img = Image.new("RGB", (largura, altura), "white")
        draw = ImageDraw.Draw(img)

        draw.point([(0, 0), (1, 0), (2, 0), (3, 0), (10, 0), (11, 0), (12, 0), (17, 0), (18, 0), (19, 0), (26, 0), (27, 0), (28, 0), (29, 0), (3, 1), (4, 1), (11, 1), (12, 1), (13, 1), (16, 1), (17, 1), (18, 1), (25, 1), (26, 1), (4, 2), (5, 2), (13, 2), (14, 2), (15, 2), (16, 2), (24, 2), (25, 2), (5, 3), (14, 3), (15, 3), (24, 3), (9, 7), (10, 7), (11, 7), (12, 7), (17, 7), (18, 7), (19, 7), (20, 7), (10, 8), (11, 8), (18, 8), (19, 8), (3, 9), (4, 9), (11, 9), (12, 9), (17, 9), (18, 9), (25, 9), (26, 9)], fill=(104, 63, 161, 247))

        draw.point([(4, 0), (14, 0), (15, 0), (25, 0)], fill=(122, 86, 172, 247))

        draw.point([(5, 0), (24, 0), (0, 1), (1, 1), (6, 1), (23, 1), (28, 1), (29, 1), (1, 2), (2, 2), (3, 2), (6, 2), (7, 2), (9, 2), (20, 2), (22, 2), (23, 2), (26, 2), (27, 2), (28, 2), (0, 3), (2, 3), (3, 3), (7, 3), (10, 3), (11, 3), (12, 3), (17, 3), (18, 3), (19, 3), (22, 3), (26, 3), (27, 3), (29, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (7, 4), (12, 4), (13, 4), (16, 4), (17, 4), (22, 4), (24, 4), (25, 4), (26, 4), (27, 4), (28, 4), (29, 4), (1, 5), (2, 5), (3, 5), (5, 5), (6, 5), (7, 5), (13, 5), (16, 5), (22, 5), (23, 5), (24, 5), (26, 5), (27, 5), (28, 5), (3, 6), (4, 6), (25, 6), (26, 6), (4, 7), (5, 7), (24, 7), (25, 7), (4, 8), (5, 8), (6, 8), (23, 8), (24, 8), (25, 8), (6, 9), (7, 9), (23, 9)], fill=(49, 22, 84, 247))

        draw.point([(6, 0), (7, 0), (22, 0), (23, 0), (7, 1), (22, 1), (8, 2), (21, 2), (8, 3), (21, 3), (0, 5), (4, 5), (25, 5), (29, 5), (1, 6), (2, 6), (5, 6), (24, 6), (27, 6), (28, 6), (3, 7), (6, 7), (23, 7), (26, 7), (7, 8), (22, 8), (0, 9), (8, 9), (21, 9), (29, 9)], fill=(74, 37, 129, 247))

        draw.point([(8, 0), (9, 0), (20, 0), (21, 0), (2, 1), (8, 1), (9, 1), (10, 1), (19, 1), (20, 1), (21, 1), (27, 1), (11, 2), (12, 2), (17, 2), (18, 2), (4, 3), (9, 3), (13, 3), (16, 3), (20, 3), (25, 3), (14, 4), (15, 4), (0, 6), (6, 6), (7, 6), (8, 6), (12, 6), (14, 6), (15, 6), (17, 6), (21, 6), (22, 6), (23, 6), (29, 6), (2, 7), (7, 7), (8, 7), (21, 7), (22, 7), (27, 7), (0, 8), (1, 8), (3, 8), (8, 8), (9, 8), (20, 8), (21, 8), (26, 8), (28, 8), (29, 8), (1, 9), (5, 9), (9, 9), (10, 9), (19, 9), (20, 9), (24, 9), (28, 9)], fill=(88, 51, 140, 247))

        draw.point([(13, 0), (16, 0), (5, 1), (14, 1), (15, 1), (24, 1), (6, 3), (23, 3), (6, 4), (23, 4), (14, 7), (15, 7), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (17, 8), (13, 9), (14, 9), (15, 9), (16, 9)], fill=(115, 78, 165, 247))

        draw.point([(0, 2), (29, 2), (1, 3), (28, 3)], fill=(192, 14, 2, 247))

        draw.point([(10, 2), (19, 2), (14, 5), (15, 5), (0, 7), (1, 7), (13, 7), (16, 7), (28, 7), (29, 7), (2, 8), (27, 8), (2, 9), (22, 9), (27, 9)], fill=(68, 30, 118, 247))

        draw.point([(8, 4), (21, 4)], fill=(88, 34, 27, 247))

        draw.point([(9, 4), (10, 4), (19, 4), (20, 4), (10, 5), (11, 5), (12, 5), (17, 5), (18, 5), (19, 5), (13, 6), (16, 6)], fill=(228, 130, 44, 247))

        draw.point([(11, 4), (18, 4)], fill=(234, 160, 23, 247))

        draw.point([(8, 5), (21, 5)], fill=(120, 41, 31, 247))

        draw.point([(9, 5), (20, 5), (9, 6), (10, 6), (11, 6), (18, 6), (19, 6), (20, 6)], fill=(178, 60, 20, 247))
        img.save(path)
        return path

    def mostrar_pixel_art_colorida_polvo(path, largura=30, altura=10):
        img = Image.open(path).convert("RGB")

        img = img.resize((largura, altura), resample=Image.NEAREST)
        pixels = img.load()

        for y in range(altura):
            linha = ""
            for x in range(largura):
                r, g, b = pixels[x, y]
                linha += f"[rgb({r},{g},{b})]█[/rgb({r},{g},{b})]"
            console.print(linha)

    caminho = criar_pixel_art()
    mostrar_pixel_art_colorida_polvo(caminho, largura=60, altura=10)

def pixel_artWIN():
    console = Console()

    def criar_pixel_art(path="win.png"):
        largura = 30
        altura = 10
        img = Image.new("RGB", (largura, altura), "white")
        draw = ImageDraw.Draw(img)

        draw.point([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (25, 0), (26, 0), (27, 0), (28, 0), (29, 0),
            (0, 1), (1, 1), (28, 1), (29, 1), (0, 2), (29, 2), (11, 8), (12, 8), (13, 8), (14, 8),
            (15, 8), (16, 8), (17, 8), (18, 8), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9),
            (15, 9), (16, 9), (17, 9), (18, 9), (19, 9), (20, 9)], fill=(78, 6, 0, 255))

        draw.point([(5, 0), (6, 0), (7, 0), (22, 0), (23, 0), (24, 0), (2, 1), (3, 1), (4, 1), (25, 1),
            (26, 1), (27, 1)], fill=(224, 75, 63, 255))

        draw.point([(8, 0), (9, 0), (10, 0), (11, 0), (18, 0), (19, 0), (20, 0), (21, 0), (5, 1), (6, 1),
            (7, 1), (8, 1), (9, 1), (10, 1), (12, 1), (13, 1), (16, 1), (17, 1), (19, 1), (20, 1),
            (21, 1), (22, 1), (23, 1), (24, 1), (4, 2), (5, 2), (8, 2), (9, 2), (10, 2), (11, 2),
            (12, 2), (13, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2), (21, 2), (22, 2), (23, 2),
            (24, 2), (25, 2), (2, 3), (3, 3), (4, 3), (6, 3), (9, 3), (11, 3), (12, 3), (13, 3),
            (16, 3), (17, 3), (18, 3), (20, 3), (21, 3), (22, 3), (25, 3), (26, 3), (27, 3), (0, 4),
            (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (9, 4), (10, 4), (11, 4), (12, 4),
            (13, 4), (16, 4), (17, 4), (18, 4), (19, 4), (20, 4), (21, 4), (24, 4), (25, 4),
            (26, 4), (27, 4), (28, 4), (29, 4), (0, 5), (2, 5), (3, 5), (4, 5), (6, 5), (7, 5),
            (10, 5), (11, 5), (18, 5), (19, 5), (24, 5), (25, 5), (26, 5), (28, 5), (29, 5), (0, 6),
            (4, 6), (10, 6), (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (19, 6), (21, 6),
            (22, 6), (24, 6), (25, 6), (28, 6), (29, 6), (0, 7), (1, 7), (2, 7), (5, 7), (7, 7),
            (8, 7), (9, 7), (10, 7), (19, 7), (20, 7), (21, 7), (22, 7), (27, 7), (28, 7), (29, 7),
            (2, 8), (3, 8), (7, 8), (8, 8), (21, 8), (22, 8), (25, 8), (26, 8), (27, 8), (2, 9),
            (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (22, 9), (23, 9), (24, 9), (25, 9), (26, 9),
            (27, 9)], fill=(218, 25, 9, 255))

        draw.point([(12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0), (11, 1), (18, 1), (7, 2), (8, 3),
            (23, 3), (8, 4), (22, 4), (1, 5), (5, 5), (9, 5), (20, 5), (27, 5), (3, 6), (6, 6),
            (26, 6), (4, 7), (24, 7)], fill=(247, 162, 45, 255))

        draw.point([(14, 1), (15, 1), (6, 2), (14, 2), (15, 2), (5, 3), (7, 3), (10, 3), (14, 3), (15, 3),
            (19, 3), (24, 3), (7, 4), (14, 4), (15, 4), (23, 4), (8, 5), (12, 5), (13, 5), (14, 5),
            (15, 5), (16, 5), (17, 5), (21, 5), (22, 5), (23, 5), (1, 6), (2, 6), (5, 6), (7, 6),
            (8, 6), (9, 6), (11, 6), (18, 6), (20, 6), (23, 6), (27, 6), (3, 7), (6, 7), (23, 7),
            (25, 7), (26, 7), (1, 8), (4, 8), (5, 8), (6, 8), (23, 8), (24, 8), (28, 8)],
            fill=(255, 148, 0, 255))

        draw.point([(1, 2), (2, 2), (3, 2), (26, 2), (27, 2), (28, 2), (0, 3), (1, 3), (28, 3), (29, 3)],
           fill=(222, 60, 47, 255))

        draw.point([(11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (17, 7), (18, 7), (0, 8), (9, 8),
            (10, 8), (19, 8), (20, 8), (29, 8), (0, 9), (1, 9), (8, 9), (21, 9), (28, 9), (29, 9)],
           fill=(181, 30, 18, 255))

        img.save(path)
        return path

    def mostrar_pixel_art_colorida_polvo(path, largura=30, altura=10):
        img = Image.open(path).convert("RGB")

        img = img.resize((largura, altura), resample=Image.NEAREST)
        pixels = img.load()

        for y in range(altura):
            linha = ""
            for x in range(largura):
                r, g, b = pixels[x, y]
                linha += f"[rgb({r},{g},{b})]█[/rgb({r},{g},{b})]"
            console.print(linha)

    caminho = criar_pixel_art()
    mostrar_pixel_art_colorida_polvo(caminho, largura=60, altura=10)

def pixel_artLOST():
    console = Console()

    def criar_pixel_art(path="lost.png"):
        largura = 30
        altura = 10
        img = Image.new("RGB", (largura, altura), "white")
        draw = ImageDraw.Draw(img)

        draw.point([(0, 0), (6, 0), (7, 0), (8, 0), (14, 0), (15, 0), (16, 0), (22, 0), (23, 0), (24, 0), (0, 1), (6, 1), (7, 1), (8, 1), (14, 1), (15, 1), (16, 1), (22, 1), (23, 1), (24, 1), (0, 2), (6, 2), (7, 2), (8, 2), (14, 2), (15, 2), (16, 2), (0, 3), (1, 3), (5, 3), (6, 3), (8, 3), (9, 3), (13, 3), (17, 3), (21, 3), (22, 3), (24, 3), (25, 3), (29, 3), (1, 4), (2, 4), (3, 4), (5, 4), (9, 4), (11, 4), (12, 4), (13, 4), (18, 4), (19, 4), (20, 4), (21, 4), (25, 4), (26, 4), (27, 4), (28, 4), (29, 4), (2, 5), (3, 5), (11, 5), (12, 5), (26, 5), (27, 5), (28, 5)], fill=((58), (30), (95), (255)))

        draw.point([(1, 0), (5, 0), (9, 0), (13, 0), (17, 0), (21, 0), (25, 0), (29, 0), (1, 1), (2, 1), (4, 1), (5, 1), (9, 1), (10, 1), (12, 1), (13, 1), (17, 1), (18, 1), (20, 1), (21, 1), (25, 1), (26, 1), (28, 1), (29, 1), (1, 2), (2, 2), (3, 2), (5, 2), (9, 2), (10, 2), (20, 2), (26, 2), (27, 2), (28, 2), (29, 2), (2, 3), (3, 3), (11, 3), (12, 3), (18, 3), (19, 3), (26, 3), (27, 3), (28, 3)], fill=((80), (34), (140), (255)))

        draw.point([(2, 0), (3, 0), (4, 0), (10, 0), (11, 0), (12, 0), (18, 0), (19, 0), (20, 0), (26, 0), (27, 0), (28, 0), (3, 1), (11, 1), (19, 1), (27, 1)], fill=((112), (47), (197), (255)))

        draw.point([(4, 2), (12, 2), (18, 2), (23, 2)], fill=((173), (68), (171), (255)))

        draw.point([(11, 2), (13, 2), (17, 2), (19, 2), (21, 2), (22, 2), (24, 2), (25, 2), (4, 3), (10, 3), (14, 3), (16, 3), (20, 3), (23, 3), (4, 4), (10, 4), (14, 4), (17, 4)], fill=((158), (54), (148), (255)))

        draw.point([(7, 3), (15, 3), (0, 4), (6, 4), (7, 4), (8, 4), (15, 4), (16, 4), (22, 4), (24, 4), (0, 5), (1, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (13, 5), (15, 5), (16, 5), (17, 5), (21, 5), (22, 5), (24, 5), (25, 5), (29, 5), (0, 6), (1, 6), (6, 6), (7, 6), (15, 6), (21, 6), (22, 6), (24, 6), (28, 6), (29, 6), (0, 7), (14, 7), (15, 7), (16, 7), (21, 7), (22, 7), (29, 7), (7, 8), (15, 8), (22, 8)], fill=((51), (24), (86), (255)))

        draw.point([(23, 4), (4, 5), (10, 5), (14, 5), (23, 5), (4, 6), (8, 6), (10, 6), (14, 6), (16, 6), (23, 6), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (11, 7), (12, 7), (13, 7), (17, 7), (18, 7), (19, 7), (20, 7), (23, 7)], fill=((160), (36), (148), (255)))

        draw.point([(18, 5), (19, 5), (20, 5), (20, 6)], fill=((162), (34), (159), (255)))

        draw.point([(2, 6), (3, 6), (5, 6), (9, 6), (11, 6), (12, 6), (13, 6), (17, 6), (18, 6), (19, 6), (25, 6), (26, 6), (27, 6), (1, 7), (2, 7), (9, 7), (10, 7), (24, 7), (25, 7), (27, 7), (28, 7), (0, 8), (1, 8), (5, 8), (6, 8), (8, 8), (9, 8), (13, 8), (14, 8), (16, 8), (17, 8), (20, 8), (21, 8), (23, 8), (24, 8), (28, 8), (29, 8), (0, 9), (6, 9), (7, 9), (8, 9), (14, 9), (15, 9), (16, 9), (21, 9), (22, 9), (23, 9), (29, 9)], fill=((43), (22), (70), (255)))

        draw.point([(3, 7), (26, 7), (2, 8), (3, 8), (4, 8), (10, 8), (11, 8), (12, 8), (18, 8), (19, 8), (25, 8), (26, 8), (27, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (17, 9), (18, 9), (19, 9), (20, 9), (24, 9), (25, 9), (26, 9), (27, 9), (28, 9)], fill=((27), (11), (47), (255)))

        img.save(path)
        return path

    def mostrar_pixel_art_colorida_polvo(path, largura=30, altura=10):
        img = Image.open(path).convert("RGB")

        img = img.resize((largura, altura), resample=Image.NEAREST)
        pixels = img.load()

        for y in range(altura):
            linha = ""
            for x in range(largura):
                r, g, b = pixels[x, y]
                linha += f"[rgb({r},{g},{b})]█[/rgb({r},{g},{b})]"
            console.print(linha)

    caminho = criar_pixel_art()
    mostrar_pixel_art_colorida_polvo(caminho, largura=60, altura=10)

def pixel_artOVO():
    console = Console()

    def criar_pixel_art(path="ovo.png"):
        largura = 30
        altura = 10
        img = Image.new("RGB", (largura, altura), "white")
        draw = ImageDraw.Draw(img)

        draw.point([(0, 0), (1, 0), (28, 0), (29, 0), (0, 1), (1, 1), (28, 1), (29, 1), (0, 2), (1, 2), (28, 2), (29, 2), (0, 3), (1, 3), (28, 3), (29, 3), (0, 4), (1, 4), (28, 4), (29, 4), (0, 5), (1, 5), (28, 5), (29, 5), (0, 6), (1, 6), (28, 6), (29, 6), (0, 7), (1, 7), (28, 7), (29, 7), (0, 8), (1, 8), (28, 8), (29, 8), (0, 9), (1, 9), (28, 9), (29, 9)], fill=((6), (6), (6), (255)))

        draw.point([(2, 0), (27, 0), (2, 1), (27, 1), (2, 2), (27, 2), (2, 3), (27, 3), (2, 4), (27, 4), (2, 5), (27, 5), (2, 6), (27, 6), (2, 7), (27, 7), (2, 8), (27, 8), (2, 9), (27, 9)], fill=((20), (36), (37), (255)))

        draw.point([(3, 0), (26, 0), (3, 1), (26, 1), (3, 2), (26, 2), (3, 3), (26, 3), (3, 4), (26, 4), (3, 5), (26, 5), (3, 6), (26, 6), (3, 7), (26, 7), (3, 8), (26, 8), (3, 9), (26, 9)], fill=((29), (56), (58), (255)))

        draw.point([(4, 0), (25, 0), (4, 1), (25, 1), (4, 2), (25, 2), (4, 3), (25, 3), (4, 4), (25, 4), (4, 5), (25, 5), (4, 6), (25, 6), (4, 7), (25, 7), (4, 8), (25, 8), (4, 9), (25, 9)], fill=((22), (69), (72), (255)))

        draw.point([(5, 0), (24, 0), (5, 1), (24, 1), (5, 2), (24, 2), (5, 3), (24, 3), (5, 4), (24, 4), (5, 5), (24, 5), (5, 6), (24, 6), (5, 7), (24, 7), (5, 8), (24, 8), (5, 9), (24, 9)], fill=((25), (105), (109), (255)))

        draw.point([(6, 0), (23, 0), (6, 1), (23, 1), (6, 2), (23, 2), (6, 3), (23, 3), (6, 4), (23, 4), (6, 5), (23, 5), (6, 6), (23, 6), (6, 7), (23, 7), (6, 8), (23, 8), (6, 9), (23, 9)], fill=((22), (136), (142), (255)))

        draw.point([(7, 0), (22, 0), (7, 1), (22, 1), (7, 2), (22, 2), (7, 3), (22, 3), (7, 4), (22, 4), (7, 5), (22, 5), (7, 6), (22, 6), (7, 7), (22, 7), (7, 8), (22, 8), (7, 9), (22, 9)], fill=((25), (54), (56), (255)))

        draw.point([(8, 0), (21, 0), (8, 1), (21, 1), (8, 2), (21, 2), (8, 3), (21, 3), (8, 4), (21, 4), (8, 5), (21, 5), (8, 6), (21, 6), (8, 7), (21, 7), (8, 8), (21, 8), (8, 9), (21, 9)], fill=((143), (214), (218), (255)))

        draw.point([(9, 0), (20, 0), (9, 1), (20, 1), (9, 2), (20, 2), (9, 3), (20, 3), (9, 4), (20, 4), (9, 5), (20, 5), (9, 6), (20, 6), (9, 7), (20, 7), (9, 8), (20, 8), (9, 9), (20, 9)], fill=((98), (202), (208), (255)))

        draw.point([(10, 0), (11, 0), (12, 0), (13, 0), (16, 0), (17, 0), (18, 0), (19, 0), (10, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1), (10, 2), (11, 2), (18, 2), (19, 2), (10, 3), (11, 3), (18, 3), (19, 3), (10, 4), (19, 4), (10, 5), (19, 5), (10, 6), (19, 6), (10, 7), (19, 7), (10, 8), (11, 8), (18, 8), (19, 8), (10, 9), (11, 9), (12, 9), (17, 9), (18, 9), (19, 9)], fill=((59), (191), (197), (255)))

        draw.point([(14, 0), (15, 0), (13, 1), (16, 1), (12, 2), (17, 2)], fill=((45), (73), (103), (255)))

        draw.point([(14, 1), (15, 1), (13, 2), (16, 2), (12, 3), (17, 3), (11, 4), (18, 4)], fill=((54), (94), (136), (255)))

        draw.point([(14, 2), (13, 3), (14, 3), (15, 4), (14, 5), (15, 5), (16, 5), (17, 5), (14, 6), (15, 6), (17, 6), (18, 6), (13, 7), (14, 7), (14, 8)], fill=((72), (133), (183), (255)))

        draw.point([(15, 2), (15, 3), (16, 3), (12, 4), (13, 4), (14, 4), (16, 4), (17, 4), (11, 5), (12, 5), (13, 5), (18, 5), (12, 6), (13, 6), (16, 6), (15, 7), (16, 7)], fill=((66), (108), (156), (255)))

        draw.point([(11, 6)], fill=((75), (142), (197), (255)))

        draw.point([(11, 7), (17, 7)], fill=((80), (124), (175), (255)))

        draw.point([(12, 7), (18, 7)], fill=((82), (147), (199), (255)))

        draw.point([(12, 8), (13, 8), (15, 8), (16, 8)], fill=((68), (122), (183), (255)))

        draw.point([(17, 8), (13, 9), (14, 9), (15, 9), (16, 9)], fill=((73), (152), (193), (255)))
        img.save(path)
        return path

    def mostrar_pixel_art_colorida_polvo(path, largura=30, altura=10):
        img = Image.open(path).convert("RGB")

        img = img.resize((largura, altura), resample=Image.NEAREST)
        pixels = img.load()

        for y in range(altura):
            linha = ""
            for x in range(largura):
                r, g, b = pixels[x, y]
                linha += f"[rgb({r},{g},{b})]█[/rgb({r},{g},{b})]"
            console.print(linha)

    caminho = criar_pixel_art()
    mostrar_pixel_art_colorida_polvo(caminho, largura=60, altura=10)

def pixel_artSTART():
    console = Console()

    def criar_pixel_art(path="start.png"):
        largura = 30
        altura = 10
        img = Image.new("RGB", (largura, altura), "white")
        draw = ImageDraw.Draw(img)

        draw.point([(0, 0), (1, 0), (28, 0), (29, 0), (0, 1), (29, 1), (0, 4), (29, 4), (0, 5), (29, 5), (0, 8), (29, 8), (0, 9), (1, 9), (28, 9), (29, 9)], fill=(229, 33, 0, 255))
        draw.point([(2, 0), (27, 0), (1, 2), (28, 2), (1, 3), (27, 3), (28, 3), (1, 4), (2, 4), (26, 4), (27, 4), (28, 4), (1, 5), (2, 5), (3, 5), (26, 5), (27, 5), (28, 5), (1, 6), (27, 6), (28, 6), (1, 7), (28, 7), (2, 9), (27, 9)], fill=(251, 40, 4, 255))
        draw.point([(3, 0), (4, 0), (25, 0), (26, 0), (2, 1), (3, 1), (26, 1), (27, 1), (2, 2), (27, 2), (25, 3), (26, 3), (25, 4), (25, 5), (25, 6), (26, 6), (2, 7), (26, 7), (27, 7), (2, 8), (3, 8), (26, 8), (27, 8), (3, 9), (4, 9), (25, 9), (26, 9)], fill=(251, 59, 2, 255))
        draw.point([(5, 0), (24, 0), (4, 1), (5, 1), (6, 1), (23, 1), (24, 1), (25, 1), (5, 4), (25, 7), (25, 8), (5, 9), (24, 9)], fill=(251, 81, 2, 255))
        draw.point([(6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (19, 0), (20, 0), (21, 0), (22, 0), (23, 0), (7, 1), (8, 1), (21, 1), (22, 1), (7, 4), (8, 4), (8, 5), (8, 6), (22, 6), (8, 7), (7, 8), (8, 8), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9), (15, 9), (16, 9), (17, 9), (18, 9), (19, 9), (20, 9), (21, 9), (22, 9), (23, 9)], fill=(251, 100, 2, 255))
        draw.point([(1, 1), (28, 1), (0, 2), (29, 2), (0, 3), (29, 3), (0, 6), (29, 6), (0, 7), (29, 7), (1, 8), (28, 8)], fill=(241, 35, 0, 255))
        draw.point([(9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (20, 5), (11, 8), (20, 8)], fill=(251, 109, 2, 255))
        draw.point([(14, 1), (15, 1), (11, 4), (11, 5), (14, 8), (15, 8)], fill=(251, 132, 2, 255))
        draw.point([(3, 2), (4, 5), (4, 6), (3, 7)], fill=(204, 50, 31, 255))
        draw.point([(4, 2), (6, 2), (9, 2), (11, 2), (14, 2), (16, 2), (19, 2), (21, 2), (23, 2), (22, 3)], fill=(48, 76, 255, 255))
        draw.point([(5, 2), (10, 2), (15, 2), (20, 2), (24, 2)], fill=(81, 104, 251, 255))
        draw.point([(7, 2), (8, 3), (21, 4), (21, 5), (21, 7), (21, 8), (22, 8)], fill=(204, 83, 31, 255))
        draw.point([(8, 2), (12, 2), (22, 2), (25, 2), (26, 2), (3, 3), (7, 3), (10, 3), (13, 3), (14, 3), (16, 3), (17, 3), (19, 3), (21, 3), (24, 3)], fill=(34, 60, 228, 255))
        draw.point([(13, 2), (12, 7), (18, 7)], fill=(204, 94, 31, 255))
        draw.point([(17, 2), (11, 7)], fill=(251, 114, 2, 255))
        draw.point([(18, 2), (18, 3), (18, 6)], fill=(204, 100, 31, 255))
        draw.point([(2, 3), (3, 4), (2, 6)], fill=(204, 35, 33, 255))
        draw.point([(4, 3)], fill=(167, 58, 54, 255))
        draw.point([(5, 3), (6, 3), (23, 3), (6, 4), (23, 4), (23, 5), (5, 6), (6, 6), (23, 6), (23, 7), (4, 8), (5, 8), (6, 8), (23, 8), (24, 8)], fill=(204, 68, 31, 255))
        draw.point([(9, 3), (20, 3), (9, 4), (20, 4), (9, 5), (9, 6), (9, 7), (20, 7), (9, 8), (10, 8), (12, 8), (13, 8), (16, 8), (17, 8), (18, 8), (19, 8)], fill=(204, 90, 31, 255))
        draw.point([(11, 3), (11, 6)], fill=(251, 121, 2, 255))
        draw.point([(12, 3), (18, 4), (18, 5), (12, 6), (16, 7)], fill=(204, 109, 31, 255))
        draw.point([(15, 3), (12, 4), (12, 5), (16, 6)], fill=(204, 114, 31, 255))
        draw.point([(4, 4), (10, 4), (13, 4), (17, 4), (19, 4), (22, 4), (24, 4)], fill=(32, 30, 199, 255))
        draw.point([(14, 4), (15, 4), (16, 4), (14, 6), (15, 6)], fill=(204, 121, 33, 255))
        draw.point([(5, 5), (6, 5), (7, 5), (10, 5), (13, 5), (14, 5), (15, 5), (16, 5), (17, 5), (19, 5), (22, 5), (24, 5), (3, 6), (7, 6), (10, 6), (13, 6), (17, 6), (19, 6), (20, 6), (21, 6), (24, 6), (4, 7), (5, 7), (6, 7), (7, 7), (10, 7), (13, 7), (17, 7), (19, 7), (22, 7), (24, 7)], fill=(17, 16, 148, 255))
        draw.point([(14, 7), (15, 7)], fill=(251, 139, 2, 255))        
        img.save(path)
        return path

    def mostrar_pixel_art_colorida_polvo(path, largura=30, altura=10):
        img = Image.open(path).convert("RGB")

        img = img.resize((largura, altura), resample=Image.NEAREST)
        pixels = img.load()

        for y in range(altura):
            linha = ""
            for x in range(largura):
                r, g, b = pixels[x, y]
                linha += f"[rgb({r},{g},{b})]█[/rgb({r},{g},{b})]"
            console.print(linha)

    caminho = criar_pixel_art()
    mostrar_pixel_art_colorida_polvo(caminho, largura=60, altura=10)

print("Sejá bem vindo!")
Inicio = input("gostaria de ler a história ou pular direto para a ação?(história ou ação): ").lower()

if Inicio == "história":
    digitar_com_pausa("""----------------------------
Seja bem vindo a Batalha Naval!
Você é o comandante da setor de defesa da Ilha ----.
Uma base secreta criada pelos militares para pesquisar um objeto misterioso que caiu na terra!
Após muita pesquisa foi descoberto que esse objeto misterioso era um ovo alienigena.""")
    pixel_artOVO()
    digitar_com_pausa("Porém o que esses pesquisadores não sabiam é que estavam atrás do pequeno alienigena...")
    pixel_artPOLVO()
    digitar_com_pausa("----------------------------")

    inicio_de_batalha()

elif Inicio == "ação":
    inicio_de_batalha()

elif Inicio == "derrota":
    pixel_artLOST
    print("\n\033[1;31mO Você perdeu! As tropas alienigenas conseguiram reguperar o pequeno alienígena.\033[0m")

elif Inicio == "vitória":
    pixel_artWIN()
    print("\n\033[1;32mParabéns! Você venceu a batalha contra os alienígenas!\033[0m")
