import random

# Função que define o que acontece quando um ataque é feito (acertando um navio ou não)
def ataque(tabuleiro_oculto, tabuleiro_visivel, coordenadas, frota):
    linha, coluna = coordenadas

    if tabuleiro_oculto[linha][coluna] != "🌊": 
        tabuleiro_visivel[linha][coluna] = "💥"
        navio_acertado = tabuleiro_oculto[linha][coluna]

        # Marca acerto na frota
        frota[navio_acertado]["atingido"].append((linha, coluna))

        # Ao afundar um navio, o jogador ou computador joga novamente
        if verificar_afundamento(frota, navio_acertado):
            print(f"Você afundou o {navio_acertado} inimigo!")
            return True
        # Ao acertar parte de um navio, a vez é passada
        else:
            print(f"Você acertou uma parte do {navio_acertado}!")
            return False
        
    # Ao errar o ataque, a vez também é passada
    else:
        tabuleiro_visivel[linha][coluna] = "❌"
        print("Você errou o tiro.")
        return False 

    # Quantidade de embarcações restantes após o ataque
    restantes = contar_embarcacoes_vivas(frota)
    print(f"Restam {restantes} navios inimigos.")

# Função que verifica um navio foi afundado (atingido em todas as suas posições)
def verificar_afundamento(frota, nome_navio):
    posicoes = frota[nome_navio]["posicoes"]
    atingidos = frota[nome_navio]["atingido"]
    return set(posicoes) == set(atingidos)

# Função que verifica se todas as embarcações foram afundadas
def todas_embarcacoes_afundadas(frota):
    for navio in frota.values():
        if set(navio["posicoes"]) != set(navio["atingido"]):
            return False
    return True

# Função que aleatoriza o ataque do computador
def escolher_ataque_aleatorio(tiros_realizados):
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        
        # Verifica que a posição randomizada já não foi jogada
        if (linha, coluna) not in tiros_realizados:
            return (linha, coluna)

# Função que verifica quantas embarcações restantes estão em cada tabuleiro
def contar_embarcacoes_vivas(frota):
    vivas = 0
    for navio in frota.values():
        if set(navio["posicoes"]) != set(navio["atingido"]):
            vivas += 1
    return vivas


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
