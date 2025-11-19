document.addEventListener('DOMContentLoaded', () => {
    // --- Elementos do DOM ---
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const scoreDisplay = document.getElementById('scoreDisplay');
    const startButton = document.getElementById('startButton');

    // --- Configurações do Jogo ---
    const TAMANHO_BLOCO = 20; // Tamanho de cada "célula" da grade
    canvas.width = 20 * TAMANHO_BLOCO; // 400px
    canvas.height = 20 * TAMANHO_BLOCO; // 400px

    const COR_FUNDO_CANVAS = '#7f8c8d'; // Cinza do style.css
    const COR_COBRA_CABECA = '#2ecc71'; // Verde esmeralda
    const COR_COBRA_CORPO = '#27ae60'; // Verde nefrita (um pouco mais escuro)
    const COR_OLHOS_COBRA = '#ffffff'; // Branco
    const COR_COMIDA = '#e74c3c'; // Vermelho alizarina
    const COR_TEXTO_GAME_OVER = '#ffffff';
    const COR_TEXTO_PONTUACAO_FINAL = '#f1c40f'; // Amarelo do style.css

    const VELOCIDADE_INICIAL = 150; // Milissegundos entre os movimentos (menor = mais rápido)
    const ACELERACAO = 5; // Quanto a velocidade diminui (em ms) a cada X pontos

    // --- Estado do Jogo ---
    let cobra;
    let comida;
    let direcao;
    let direcaoBuffer; // Para armazenar a próxima direção e evitar auto-colisão em movimentos rápidos
    let pontuacao;
    let velocidadeAtual;
    let gameRodando = false;
    let gameOver = false;
    let loopJogoTimeout;

    // --- Funções de Desenho Detalhado ---

    function desenharBlocoArredondado(x, y, largura, altura, raio, cor) {
        ctx.fillStyle = cor;
        ctx.beginPath();
        ctx.moveTo(x + raio, y);
        ctx.lineTo(x + largura - raio, y);
        ctx.quadraticCurveTo(x + largura, y, x + largura, y + raio);
        ctx.lineTo(x + largura, y + altura - raio);
        ctx.quadraticCurveTo(x + largura, y + altura, x + largura - raio, y + altura);
        ctx.lineTo(x + raio, y + altura);
        ctx.quadraticCurveTo(x, y + altura, x, y + altura - raio);
        ctx.lineTo(x, y + raio);
        ctx.quadraticCurveTo(x, y, x + raio, y);
        ctx.closePath();
        ctx.fill();
    }

    function desenharCabecaCobra(x, y) {
        desenharBlocoArredondado(x, y, TAMANHO_BLOCO, TAMANHO_BLOCO, 5, COR_COBRA_CABECA);

        // Desenhar olhos dependendo da direção
        ctx.fillStyle = COR_OLHOS_COBRA;
        const tamanhoOlho = TAMANHO_BLOCO / 5;
        const offsetOlho1 = TAMANHO_BLOCO / 4;
        const offsetOlho2 = TAMANHO_BLOCO - TAMANHO_BLOCO / 4 - tamanhoOlho;

        if (direcao.x === 1) { // Direita
            ctx.fillRect(x + offsetOlho2, y + offsetOlho1, tamanhoOlho, tamanhoOlho);
            ctx.fillRect(x + offsetOlho2, y + offsetOlho2, tamanhoOlho, tamanhoOlho);
        } else if (direcao.x === -1) { // Esquerda
            ctx.fillRect(x + offsetOlho1, y + offsetOlho1, tamanhoOlho, tamanhoOlho);
            ctx.fillRect(x + offsetOlho1, y + offsetOlho2, tamanhoOlho, tamanhoOlho);
        } else if (direcao.y === 1) { // Baixo
            ctx.fillRect(x + offsetOlho1, y + offsetOlho2, tamanhoOlho, tamanhoOlho);
            ctx.fillRect(x + offsetOlho2, y + offsetOlho2, tamanhoOlho, tamanhoOlho);
        } else if (direcao.y === -1) { // Cima
            ctx.fillRect(x + offsetOlho1, y + offsetOlho1, tamanhoOlho, tamanhoOlho);
            ctx.fillRect(x + offsetOlho2, y + offsetOlho1, tamanhoOlho, tamanhoOlho);
        } else { // Parada no início
            ctx.fillRect(x + offsetOlho1, y + offsetOlho1, tamanhoOlho, tamanhoOlho);
            ctx.fillRect(x + offsetOlho2, y + offsetOlho1, tamanhoOlho, tamanhoOlho);
        }
    }

    function desenharCorpoCobra() {
        for (let i = 1; i < cobra.length; i++) {
            desenharBlocoArredondado(cobra[i].x, cobra[i].y, TAMANHO_BLOCO, TAMANHO_BLOCO, 3, COR_COBRA_CORPO);
        }
    }

    function desenharComida() {
        desenharBlocoArredondado(comida.x, comida.y, TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO / 2, COR_COMIDA); // Círculo
        // Adicionar um pequeno "brilho"
        ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
        ctx.beginPath();
        ctx.arc(comida.x + TAMANHO_BLOCO / 3, comida.y + TAMANHO_BLOCO / 3, TAMANHO_BLOCO / 5, 0, Math.PI * 2);
        ctx.fill();
    }

    function limparCanvas() {
        ctx.fillStyle = COR_FUNDO_CANVAS;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    }

    function mostrarMensagemGameOver() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.7)'; // Fundo semi-transparente
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.font = 'bold 48px Segoe UI, sans-serif';
        ctx.fillStyle = COR_TEXTO_GAME_OVER;
        ctx.textAlign = 'center';
        ctx.fillText('GAME OVER', canvas.width / 2, canvas.height / 2 - 40);

        ctx.font = '24px Segoe UI, sans-serif';
        ctx.fillStyle = COR_TEXTO_PONTUACAO_FINAL;
        ctx.fillText(`Pontuação Final: ${pontuacao}`, canvas.width / 2, canvas.height / 2 + 10);

        ctx.font = '18px Segoe UI, sans-serif';
        ctx.fillStyle = COR_TEXTO_GAME_OVER;
        ctx.fillText('Pressione "Iniciar Jogo" para tentar novamente', canvas.width / 2, canvas.height / 2 + 60);
    }


    // --- Lógica do Jogo ---
    function gerarPosicaoComida() {
        let novaPosicao;
        let sobreCobra;
        do {
            sobreCobra = false;
            novaPosicao = {
                x: Math.floor(Math.random() * (canvas.width / TAMANHO_BLOCO)) * TAMANHO_BLOCO,
                y: Math.floor(Math.random() * (canvas.height / TAMANHO_BLOCO)) * TAMANHO_BLOCO
            };
            // Verifica se a nova posição está sobre a cobra
            for (const segmento of cobra) {
                if (segmento.x === novaPosicao.x && segmento.y === novaPosicao.y) {
                    sobreCobra = true;
                    break;
                }
            }
        } while (sobreCobra);
        return novaPosicao;
    }

    function atualizarJogo() {
        if (gameOver) return;

        // Atualiza a direção com base no buffer (evita auto-colisão em movimentos rápidos)
        if (direcaoBuffer) {
            // Não permite movimento na direção oposta
            if (!((direcaoBuffer.x === -direcao.x && direcao.x !== 0) ||
                  (direcaoBuffer.y === -direcao.y && direcao.y !== 0))) {
                direcao = direcaoBuffer;
            }
            direcaoBuffer = null; // Limpa o buffer
        }


        const cabeca = { x: cobra[0].x + direcao.x * TAMANHO_BLOCO, y: cobra[0].y + direcao.y * TAMANHO_BLOCO };

        // Colisão com paredes
        if (cabeca.x < 0 || cabeca.x >= canvas.width || cabeca.y < 0 || cabeca.y >= canvas.height) {
            gameOver = true;
            return;
        }

        // Colisão com o próprio corpo
        for (let i = 1; i < cobra.length; i++) {
            if (cabeca.x === cobra[i].x && cabeca.y === cobra[i].y) {
                gameOver = true;
                return;
            }
        }

        cobra.unshift(cabeca); // Adiciona nova cabeça

        // Colisão com comida
        if (cabeca.x === comida.x && cabeca.y === comida.y) {
            pontuacao += 10;
            scoreDisplay.textContent = `Pontuação: ${pontuacao}`;
            comida = gerarPosicaoComida();
            // Aumentar velocidade
            if (pontuacao % 50 === 0 && velocidadeAtual > 50) { // A cada 50 pontos, não menor que 50ms
                velocidadeAtual -= ACELERACAO * 5; // Acelera mais rápido
                 if (velocidadeAtual < 50) velocidadeAtual = 50;
            }
        } else {
            cobra.pop(); // Remove a cauda se não comeu
        }
    }

    // --- Loop Principal e Controles ---
    function loopJogo() {
        if (gameOver) {
            mostrarMensagemGameOver();
            startButton.textContent = "Tentar Novamente";
            startButton.disabled = false;
            gameRodando = false;
            return;
        }

        limparCanvas();
        atualizarJogo(); // Mover cobra e verificar colisões está aqui dentro agora

        if (!gameOver) { // Só desenha se não for game over após a atualização
            desenharComida();
            desenharCorpoCobra(); // Desenha o corpo primeiro
            desenharCabecaCobra(cobra[0].x, cobra[0].y); // Desenha a cabeça por cima
        }

        // Próximo frame do jogo
        clearTimeout(loopJogoTimeout); // Limpa timeout anterior, se houver
        loopJogoTimeout = setTimeout(loopJogo, velocidadeAtual);
    }

    function iniciarNovoJogo() {
        cobra = [
            { x: Math.floor(canvas.width / (2 * TAMANHO_BLOCO)) * TAMANHO_BLOCO, y: Math.floor(canvas.height / (2 * TAMANHO_BLOCO)) * TAMANHO_BLOCO }, // Cabeça no centro
            // { x: Math.floor(canvas.width / (2 * TAMANHO_BLOCO)) * TAMANHO_BLOCO - TAMANHO_BLOCO, y: Math.floor(canvas.height / (2 * TAMANHO_BLOCO)) * TAMANHO_BLOCO }, // Segmento inicial do corpo
        ];
        comida = gerarPosicaoComida(); // Gera comida após a cobra ser inicializada
        direcao = { x: 0, y: 0 }; // Começa parada
        direcaoBuffer = { x: 1, y: 0 }; // Pronta para mover para a direita ao primeiro input ou automaticamente
        pontuacao = 0;
        velocidadeAtual = VELOCIDADE_INICIAL;
        gameOver = false;
        gameRodando = true;

        scoreDisplay.textContent = `Pontuação: ${pontuacao}`;
        startButton.textContent = "Jogo em Andamento...";
        startButton.disabled = true;

        limparCanvas(); // Limpa qualquer mensagem de game over anterior
        desenharComida();
        desenharCabecaCobra(cobra[0].x, cobra[0].y);

        clearTimeout(loopJogoTimeout); // Garante que não haja loops antigos rodando
        loopJogoTimeout = setTimeout(loopJogo, velocidadeAtual); // Inicia o loop com um pequeno delay
    }

    function tratarInputTeclado(evento) {
        if (!gameRodando && evento.key !== 'Enter' && evento.key !== ' ') return; // Permite iniciar com Enter/Espaço se o botão for focado

        const TECLA_ESQUERDA = 'ArrowLeft';
        const TECLA_DIREITA = 'ArrowRight';
        const TECLA_CIMA = 'ArrowUp';
        const TECLA_BAIXO = 'ArrowDown';

        // Se o jogo não começou e uma tecla de seta é pressionada, inicia o jogo
        if (!gameRodando && [TECLA_ESQUERDA, TECLA_DIREITA, TECLA_CIMA, TECLA_BAIXO].includes(evento.key)) {
             if (!gameOver) { // Só inicia se não estiver numa tela de game over (o botão cuida disso)
                iniciarNovoJogo();
            }
        }


        // Buffer para a próxima direção. Isso ajuda a registrar inputs rápidos
        // e impede que a cobra se inverta sobre si mesma imediatamente.
        switch (evento.key) {
            case TECLA_ESQUERDA:
                if (direcao.x === 0) direcaoBuffer = { x: -1, y: 0 };
                break;
            case TECLA_DIREITA:
                if (direcao.x === 0) direcaoBuffer = { x: 1, y: 0 };
                break;
            case TECLA_CIMA:
                if (direcao.y === 0) direcaoBuffer = { x: 0, y: -1 };
                break;
            case TECLA_BAIXO:
                if (direcao.y === 0) direcaoBuffer = { x: 0, y: 1 };
                break;
        }
        evento.preventDefault(); // Evita que a página role com as setas
    }

    // --- Inicialização ---
    startButton.addEventListener('click', iniciarNovoJogo);
    document.addEventListener('keydown', tratarInputTeclado);

    // Desenha um estado inicial no canvas (opcional, ou uma tela de "pressione iniciar")
    function mostrarTelaPreJogo() {
        limparCanvas();
        ctx.font = 'bold 30px Segoe UI, sans-serif';
        ctx.fillStyle = COR_COBRA_CABECA;
        ctx.textAlign = 'center';
        ctx.fillText('Jogo da Cobrinha!', canvas.width / 2, canvas.height / 2 - 20);
        ctx.font = '18px Segoe UI, sans-serif';
        ctx.fillStyle = '#ffffff';
        ctx.fillText('Clique em "Iniciar Jogo" para começar', canvas.width / 2, canvas.height / 2 + 20);
    }
    mostrarTelaPreJogo(); // Mostra a tela inicial no canvas

}); // Fim do DOMContentLoaded