
# Crie uma função que receba um nome e imprima uma saudação personalizada.

# def saudacao():
#     nome = input("Digite o seu nome: ")
#     print(f"Olá, {nome}! Seja bem-vindo(a) ao curso de Python!")

# saudacao()


# Crie uma função que receba dois números e retorne sua soma.

# def soma():
#     a = int(input("Digite o primeiro número: "))
#     b = int(input("Digite o segundo número: "))
#     resultado = a + b
#     print(f"a soma de {a} e {b} é {resultado}")
# soma()


# Escreva uma função que calcule o quadrado de um número.

# def square():
#     n = int(input("digite o número que deseja elevar ao quadrado: "))
#     s = n ** 2
#     print(f"{n} elevado ao quadrado é igual a {s}")
# square()


# Escreva uma função que verifique se um número é par.

# def par():
#     n = int(input("Digite o número que deseja verificar se é par: "))
#     if n % 2 == 0:
#         print(f"O número {n} é par")
#     else:
#         print(f"O número {n} é ímpar")
# par()


# Escreva uma função que receba uma lista de números e retorne o maior elemento.

# def lista():
#     l = (input("Digite os números da lista separados por espaço: "))
#     s = [int(num) for num in l.split()]
#     m = max(s)
#     print("O maior número da lista é:", m)
# lista()


# Crie uma função que calcule o fatorial de um número (sem usar recursão).

def fato(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("Digite o número: "))
r = fato(n)
print(f"O fatorial de {n} é igual a {r}")


# Crie uma função que receba um número e retorne True se ele for primo.

# Crie uma função que inverta uma string.

# Crie uma função que receba uma lista de nomes e retorne apenas os nomes com mais de 5 letras.

# Escreva uma função que conte quantas vogais há em uma string.

# Crie uma função que receba um número e retorne uma lista com todos os divisores dele.

# Crie uma função que converta graus Celsius para Fahrenheit.

# Crie uma função que receba uma string e retorne a mesma string sem espaços.

# Crie uma função que receba uma lista e retorne a média dos elementos.

# Escreva uma função que receba uma palavra e retorne True se ela for um palíndromo.

# Crie uma função que gere uma lista com os n primeiros números pares.

# Escreva uma função que receba um número e retorne a tabuada dele (de 1 a 10).

# Crie uma função que calcule a área de um retângulo (base × altura).

# Crie uma função que retorne o menor valor entre três números.

# Escreva uma função que simule o lançamento de um dado de 6 faces (use random.randint).

# 🟡 Exercícios Intermediários (21–40)
# Crie uma função que receba uma lista de números e retorne uma nova lista com os números elevados ao quadrado.

# Crie uma função que calcule a soma dos dígitos de um número inteiro.

# Escreva uma função que receba uma frase e retorne a quantidade de palavras.

# Crie uma função que substitua todas as vogais de uma string por "*".

# Crie uma função que receba uma lista e retorne os elementos únicos (sem usar set).

# Crie uma função que receba uma lista e um número n, e retorne os n maiores valores da lista.

# Escreva uma função que calcule a área de um triângulo (base × altura ÷ 2).

# Crie uma função recursiva para calcular o fatorial de um número.

# Crie uma função recursiva que calcule o n-ésimo número da sequência de Fibonacci.

# Escreva uma função que embaralhe os caracteres de uma string (use random.shuffle).

# Crie uma função que simule uma calculadora simples (operações: +, -, *, /), com três parâmetros: número 1, número 2 e operação.

# Crie uma função que retorne os números pares de uma lista usando list comprehension.

# Escreva uma função que recebe um número decimal e retorna sua representação binária.

# Escreva uma função que receba uma lista e retorne um dicionário com a contagem de cada elemento.

# Crie uma função que receba uma data (dia, mês, ano) e diga se ela é válida (considere apenas datas do calendário gregoriano, sem considerar anos bissextos).

# Escreva uma função que identifique o segundo maior número em uma lista.

# Crie uma função que receba uma lista de strings e retorne a maior delas.

# Escreva uma função que calcule a distância entre dois pontos (x1, y1) e (x2, y2).

# Crie uma função que receba o valor de uma compra e retorne o valor com 10% de desconto.

# Crie uma função que calcule juros compostos: montante = capital * (1 + taxa) ** tempo.

# 🔴 Exercícios Avançados (41–50)
# Crie uma função decoradora que registre o tempo de execução de outra função.

# Crie uma função que retorne uma função interna (closure) que acumula valores.

# Crie uma função que receba um CPF em formato string e valide-o.

# Escreva uma função que leia um arquivo texto e conte quantas palavras ele possui.

# Crie uma função que use filter() e lambda para filtrar números maiores que 10 de uma lista.

# Escreva uma função que utilize zip para unir duas listas em um dicionário.

# Escreva uma função que leia uma matriz (lista de listas) e retorne sua transposta.

# Crie uma função que gere senhas seguras com letras, números e símbolos (use random.choice).

# Crie uma função que detecte anagramas entre duas palavras.

# Crie uma função que verifique se uma Sudoku 9x9 está corretamente preenchida (sem números repetidos por linha, coluna e região 3x3).