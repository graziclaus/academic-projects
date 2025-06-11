import re
import shutil
import random

mar = "🌊"

def criar_tabuleiro():
    return [[mar for _ in range(10)] for _ in range(5)]

def print_tabuleiros(tabuleiro_visivel_jogador, tabuleiro_visivel_computador):
    largura_terminal = shutil.get_terminal_size().columns
    letras_colunas = [chr(i) for i in range(65, 75)]
    espacos_titulo = max((largura_terminal - 70) // 2, 0)
    print("\n" + " " * 30 + "\033[1;36mSEU TABULEIRO\033[0m" + " " * 20 + "\033[1;32mTABULEIRO DO COMPUTADOR\033[0m\n")
    letras = '   ' + ' '.join([f' {l} ' for l in letras_colunas])
    print('' * espacos_titulo + letras + ' ' * 10 + letras)
    for i in range(5):
        linha_jogador = ' │ '.join(tabuleiro_visivel_jogador[i])
        linha_computador = ' │ '.join(tabuleiro_visivel_computador[i])
        print(f"{i+1:<2} {linha_jogador}     {i+1:<2} {linha_computador}")

def verificar_posicoes_livres(tabuleiro, posicoes):
    for linha, coluna in posicoes:
        if tabuleiro[linha][coluna] != mar:
            return False
    return True

def colocar_navio(tabuleiro, posicoes, emoji):
    for linha, coluna in posicoes:
        tabuleiro[linha][coluna] = emoji

def escolha_jogador(tabuleiro_oculto_jogador, tamanhos_navios, emojis_navios):
    for nome, tamanho in tamanhos_navios.items():
        while True:
            print(f"\nPosicione seu navio: {nome.upper()} ({tamanho} espaços)")
            print_tabuleiros(tabuleiro_oculto_jogador, criar_tabuleiro())  # Só mostra o do jogador
            try:
                linha = int(input("Linha inicial (1-5): ")) - 1
            except ValueError:
                print("Linha inválida.")
                continue
            coluna = input("Coluna inicial (A-J): ").upper()
            direcao = input("Direção (Horizontal/Vertical): ").lower()
            if not (0 <= linha < 5) or coluna not in "ABCDEFGHIJ" or direcao not in ["horizontal", "vertical"]:
                print("Entrada inválida.")
                continue
            coluna = ord(coluna) - ord('A')
            if direcao == "horizontal":
                if coluna + tamanho > 10:
                    print("Navio não cabe horizontalmente.")
                    continue
                posicoes = [(linha, coluna + i) for i in range(tamanho)]
            else:
                if linha + tamanho > 5:
                    print("Navio não cabe verticalmente.")
                    continue
                posicoes = [(linha + i, coluna) for i in range(tamanho)]
            if not verificar_posicoes_livres(tabuleiro_oculto_jogador, posicoes):
                print("Já tem navio nessa posição.")
                continue
            colocar_navio(tabuleiro_oculto_jogador, posicoes, emojis_navios[nome])
            break

def escolha_computador(tabuleiro_oculto_computador, tamanhos_navios):
    for tamanho in tamanhos_navios.values():
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
                colocar_navio(tabuleiro_oculto_computador, posicoes, "🐙")
                break

def ataque(tabuleiro_oculto, tabuleiro_visivel, is_jogador):
    while True:
        if is_jogador:
            try:
                linha = int(input("Atacar linha (1-5): ")) - 1
            except ValueError:
                print("Linha inválida.")
                continue
            coluna = input("Atacar coluna (A-J): ").upper()
            if not (0 <= linha < 5) or coluna not in "ABCDEFGHIJ":
                print("Entrada inválida.")
                continue
            coluna = ord(coluna) - ord('A')
        else:
            linha = random.randint(0, 4)
            coluna = random.randint(0, 9)
        if tabuleiro_visivel[linha][coluna] != mar:
            if is_jogador:
                print("Já atacou aqui.")
            continue
        if tabuleiro_oculto[linha][coluna] != mar:
            tabuleiro_visivel[linha][coluna] = '💥'
            if is_jogador:
                print("Acertou! Jogue novamente.")
            else:
                print(f"Computador acertou em {linha+1}{chr(coluna+65)}!")
            return True
        else:
            tabuleiro_visivel[linha][coluna] = '❌'
            if is_jogador:
                print("Água!")
            else:
                print(f"Computador errou em {linha+1}{chr(coluna+65)}.")
            return False

def fim_jogo(tabuleiro_oculto, tabuleiro_visivel):
    for i in range(5):
        for j in range(10):
            if tabuleiro_oculto[i][j] != mar and tabuleiro_visivel[i][j] != '💥':
                return False
    return True

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

    escolha_jogador(tabuleiro_oculto_jogador, tamanhos_navios, emojis_navios)
    escolha_computador(tabuleiro_oculto_computador, tamanhos_navios)

    turno_jogador = True
    while True:
        print_tabuleiros(tabuleiro_visivel_jogador, tabuleiro_visivel_computador)
        if turno_jogador:
            print("\nSua vez de atacar!")
            acertou = ataque(tabuleiro_oculto_computador, tabuleiro_visivel_computador, True)
        else:
            print("\nVez do computador atacar!")
            acertou = ataque(tabuleiro_oculto_jogador, tabuleiro_visivel_jogador, False)
        if not acertou:
            turno_jogador = not turno_jogador
        if fim_jogo(tabuleiro_oculto_computador, tabuleiro_visivel_computador):
            print("\nVocê venceu!")
            break
        if fim_jogo(tabuleiro_oculto_jogador, tabuleiro_visivel_jogador):
            print("\nO computador venceu!")
            break

if __name__ == "__main__":
    main()

