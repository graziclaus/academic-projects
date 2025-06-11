import random

# Exemplo de frota
frota = {
    '🛥️': {'tamanho': 1, 'posicoes': [(0, 0)], 'atingido': []},
    '🛢️': {'tamanho': 4, 'posicoes': [(1, 0), (1, 1), (1, 2), (1, 3)], 'atingido': []}
}

def verificar_afundamento(frota, navio):
    return set(frota[navio]["posicoes"]) == set(frota[navio]["atingido"])

def ataque(tabuleiro_oculto, tabuleiro_visivel, coordenadas, frota):
    linha, coluna = coordenadas

    if tabuleiro_oculto[linha][coluna] != "🌊":
        tabuleiro_visivel[linha][coluna] = "💥"
        navio_acertado = tabuleiro_oculto[linha][coluna]
        frota[navio_acertado]["atingido"].append((linha, coluna))

        if verificar_afundamento(frota, navio_acertado):
            print(f"Você afundou o {navio_acertado} inimigo!")
            return True
        else:
            print(f"Você acertou o {navio_acertado}!")
            return True
    else:
        tabuleiro_visivel[linha][coluna] = "❌"
        print("Errou o tiro!")
        return False

# TESTE RÁPIDO
def criar_tabuleiro_vazio():
    return [["🌊" for _ in range(10)] for _ in range(10)]

# Teste com mini cenário
tab_oculto = criar_tabuleiro_vazio()
tab_visivel = criar_tabuleiro_vazio()

# Coloca os navios visivelmente no tabuleiro oculto (o real do inimigo)
for navio, info in frota.items():
    for linha, col in info["posicoes"]:
        tab_oculto[linha][col] = navio

# Atacando uma posição com navio
ataque(tab_oculto, tab_visivel, (1, 1), frota)
# Atacando água
ataque(tab_oculto, tab_visivel, (5, 5), frota)



# Função de ataque
# --> Jogador informa coordenadas
# --> Computador escolhe aleatoriamente uma coordenada ainda não usada
# Verificação se foi acerto ou erro
# Atualizar o tabuleiro visível com "X" ou "O" (?)
# Detectar se um navio foi completamente afundado
# Controlar quem joga novamente (caso afunde o navio)
# Controlar a quantidade de embarcações vivas
# Neste modo a embarcação só afunda quando todas as posições
# dela tiverem sido atingidas. Quando uma embarcação tiver todas as suas partes atingidas, a
# embarcação é então afundada e o jogador pode atacar novamente.
