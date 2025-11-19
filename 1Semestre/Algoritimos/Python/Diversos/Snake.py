import pygame
import random
import sys # Usaremos sys.exit() para fechar o jogo de forma limpa

# Inicializando o Pygame
pygame.init()

# --- Definição de Cores (RGB) ---
# Usaremos cores vibrantes como você pediu!
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (213, 50, 80)       # Cor para a comida
VERDE_ESCURO = (0, 100, 0)     # Cor para a cobra
VERDE_CLARO = (0, 200, 0)      # Cor alternativa para a cobra ou detalhes
AZUL_FUNDO = (50, 153, 213)    # Cor para o fundo
AMARELO_TEXTO = (255, 255, 102) # Cor para textos de pontuação e mensagens
CINZA_CLARO = (200, 200, 200)  # Para bordas ou elementos de UI

# --- Configurações da Tela ---
LARGURA_TELA = 600
ALTURA_TELA = 400
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Jogo da Cobrinha Colorido!')

# --- Configurações do Jogo ---
TAMANHO_BLOCO = 20  # Tamanho de cada bloco da cobra e da comida
VELOCIDADE_COBRA_INICIAL = 10 # Velocidade inicial da cobra (frames por segundo)

# Relógio para controlar a taxa de atualização da tela (FPS)
relogio = pygame.time.Clock()

# Fonte para texto
FONTE_PADRAO = pygame.font.SysFont('arial', 25) # Fonte para pontuação
FONTE_TITULO = pygame.font.SysFont('comicsansms', 50) # Fonte para títulos (Game Over, etc.)
FONTE_PEQUENA = pygame.font.SysFont('arial', 18) # Fonte para instruções

# --- Funções Auxiliares ---

def desenhar_grade():
    """Desenha uma grade sutil no fundo (opcional, para visualização)."""
    for x in range(0, LARGURA_TELA, TAMANHO_BLOCO):
        pygame.draw.line(tela, CINZA_CLARO, (x, 0), (x, ALTURA_TELA))
    for y in range(0, ALTURA_TELA, TAMANHO_BLOCO):
        pygame.draw.line(tela, CINZA_CLARO, (0, y), (LARGURA_TELA, y))

def desenhar_cobra(corpo_cobra):
    """Desenha a cobra na tela."""
    for i, segmento in enumerate(corpo_cobra):
        cor = VERDE_ESCURO if i == 0 else VERDE_CLARO # Cabeça de cor diferente
        pygame.draw.rect(tela, cor, [segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO])
        # Adicionando uma borda mais escura para melhor definição
        pygame.draw.rect(tela, PRETO, [segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO], 1)


def desenhar_comida(posicao_comida):
    """Desenha a comida na tela."""
    pygame.draw.rect(tela, VERMELHO, [posicao_comida[0], posicao_comida[1], TAMANHO_BLOCO, TAMANHO_BLOCO])
    pygame.draw.rect(tela, PRETO, [posicao_comida[0], posicao_comida[1], TAMANHO_BLOCO, TAMANHO_BLOCO], 1)


def mostrar_pontuacao(pontuacao):
    """Exibe a pontuação na tela."""
    texto_surface = FONTE_PADRAO.render("Pontuação: " + str(pontuacao), True, AMARELO_TEXTO)
    tela.blit(texto_surface, [10, 10])


def gerar_posicao_comida(corpo_cobra):
    """Gera uma nova posição aleatória para a comida, fora do corpo da cobra."""
    while True:
        x = random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO + 1, TAMANHO_BLOCO)
        y = random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO + 1, TAMANHO_BLOCO)
        nova_posicao = [x, y]
        if nova_posicao not in corpo_cobra: # Garante que não apareça sobre a cobra
            return nova_posicao

def mensagem_na_tela(msg, cor, fonte, y_desloc=0, x_centro=LARGURA_TELA / 2):
    """Exibe uma mensagem centralizada na tela."""
    texto_surface = fonte.render(msg, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = (x_centro, ALTURA_TELA / 2 + y_desloc)
    tela.blit(texto_surface, texto_rect)

# --- Tela Inicial ---
def tela_inicial():
    intro = True
    while intro:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                intro = False # Sai da tela inicial ao pressionar qualquer tecla

        tela.fill(AZUL_FUNDO)
        mensagem_na_tela("Jogo da Cobrinha!", VERDE_ESCURO, FONTE_TITULO, -50)
        mensagem_na_tela("Use as teclas de SETA para mover", AMARELO_TEXTO, FONTE_PADRAO, 20)
        mensagem_na_tela("Pressione qualquer tecla para começar", BRANCO, FONTE_PEQUENA, 60)
        pygame.display.flip()
        relogio.tick(15) # FPS baixo para a tela inicial

# --- Tela de Game Over ---
def tela_game_over(pontuacao):
    game_over = True
    while game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r: # Tecla 'R' para reiniciar
                    rodar_jogo() # Chama a função principal do jogo novamente
                if evento.key == pygame.K_s: # Tecla 'S' para sair
                    pygame.quit()
                    sys.exit()

        tela.fill(AZUL_FUNDO)
        mensagem_na_tela("GAME OVER", VERMELHO, FONTE_TITULO, -80)
        mensagem_na_tela(f"Sua pontuação final: {pontuacao}", AMARELO_TEXTO, FONTE_PADRAO, 0)
        mensagem_na_tela("Pressione 'R' para jogar novamente", BRANCO, FONTE_PEQUENA, 60)
        mensagem_na_tela("Pressione 'S' para sair", BRANCO, FONTE_PEQUENA, 90)
        pygame.display.flip()
        relogio.tick(15)


# --- Loop Principal do Jogo ---
def rodar_jogo():
    game_ativo = True
    game_fim = False # Controla se o jogo acabou e deve ir para a tela de Game Over

    # Posição inicial da cobra (centro da tela)
    # Arredondando para o múltiplo mais próximo do TAMANHO_BLOCO
    x_inicial = round((LARGURA_TELA / 2 - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
    y_inicial = round((ALTURA_TELA / 2 - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO

    pos_x_cobra = x_inicial
    pos_y_cobra = y_inicial

    # Mudança de posição inicial (parada no início)
    delta_x = 0
    delta_y = 0

    corpo_cobra = []
    comprimento_cobra = 1 # Comprimento inicial
    pontuacao = 0
    velocidade_cobra_atual = VELOCIDADE_COBRA_INICIAL

    posicao_comida = gerar_posicao_comida(corpo_cobra)

    while game_ativo:
        while game_fim: # Loop da tela de Game Over
            tela_game_over(pontuacao)

        # --- Processamento de Eventos ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: # Evento de fechar a janela
                game_ativo = False
            if evento.type == pygame.KEYDOWN: # Evento de tecla pressionada
                if evento.key == pygame.K_LEFT and delta_x == 0: # Evita mover para trás
                    delta_x = -TAMANHO_BLOCO
                    delta_y = 0
                elif evento.key == pygame.K_RIGHT and delta_x == 0:
                    delta_x = TAMANHO_BLOCO
                    delta_y = 0
                elif evento.key == pygame.K_UP and delta_y == 0:
                    delta_y = -TAMANHO_BLOCO
                    delta_x = 0
                elif evento.key == pygame.K_DOWN and delta_y == 0:
                    delta_y = TAMANHO_BLOCO
                    delta_x = 0

        # --- Lógica de Atualização do Jogo ---

        # Verifica colisão com as bordas da tela
        if pos_x_cobra >= LARGURA_TELA or pos_x_cobra < 0 or pos_y_cobra >= ALTURA_TELA or pos_y_cobra < 0:
            game_fim = True # Fim de jogo

        # Atualiza a posição da cabeça da cobra
        pos_x_cobra += delta_x
        pos_y_cobra += delta_y

        # Adiciona a nova cabeça ao corpo da cobra
        cabeca_cobra = [pos_x_cobra, pos_y_cobra]
        corpo_cobra.append(cabeca_cobra) # Adiciona no final

        # Mantém o tamanho da cobra (remove o último segmento se não comeu)
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0] # Remove o segmento mais antigo (a cauda)

        # Verifica colisão da cabeça com o próprio corpo (exceto a própria cabeça)
        for segmento in corpo_cobra[:-1]: # Percorre todos menos o último (a cabeça atual)
            if segmento == cabeca_cobra:
                game_fim = True # Fim de jogo

        # Verifica se a cobra comeu a comida
        if pos_x_cobra == posicao_comida[0] and pos_y_cobra == posicao_comida[1]:
            posicao_comida = gerar_posicao_comida(corpo_cobra)
            comprimento_cobra += 1
            pontuacao += 10
            # Aumenta a velocidade a cada 5 comidas (opcional, para dificuldade)
            if pontuacao % 50 == 0 and pontuacao > 0:
                velocidade_cobra_atual += 1


        # --- Desenho na Tela ---
        tela.fill(AZUL_FUNDO) # Preenche o fundo
        # desenhar_grade() # Descomente para ver a grade
        desenhar_comida(posicao_comida)
        desenhar_cobra(corpo_cobra)
        mostrar_pontuacao(pontuacao)

        pygame.display.flip() # Atualiza a tela inteira para mostrar o que foi desenhado

        # Controla a velocidade do jogo
        relogio.tick(velocidade_cobra_atual)

    # Sai do Pygame e do programa
    pygame.quit()
    sys.exit()

# --- Execução Principal ---
if __name__ == '__main__':
    tela_inicial()
    rodar_jogo()