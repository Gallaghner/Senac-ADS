# 1. Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def mostrar_endereco(self):
        print(f"Endereço: {self.endereco}")
    
    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco


# 2. Classe Aluno
class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    
    def mostrar_curso(self):
        print(f"Curso: {self.curso}")
    
    def alterar_curso(self, novo_curso):
        self.curso = novo_curso


# 3. Classe AlunoNotas
class AlunoNotas:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def get_nome(self):
        return self.nome
    
    def get_media(self):
        media = (self.nota1 + self.nota2 + self.nota3) / 3
        return media
    
    def aprovado(self):
        if self.get_media() >= 6:
            return True
        else:
            return False


def exercicio3():
    alunos = []
    print("\n=== Exercício 3 ===")
    
    # (a) Entrada de dados de 5 alunos
    i = 0
    while i < 5:
        print(f"\nAluno {i+1}:")
        mat = input("Matrícula: ")
        nome = input("Nome: ")
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        n3 = float(input("Nota 3: "))
        alunos.append(AlunoNotas(mat, nome, n1, n2, n3))
        i = i + 1
    
    # (b) Maior média
    maior_media = 0
    aluno_maior = None
    for aluno in alunos:
        if aluno.get_media() > maior_media:
            maior_media = aluno.get_media()
            aluno_maior = aluno
    print(f"\nMaior média: {aluno_maior.get_nome()} com {maior_media:.2f}")
    
    # (c) Menor média
    menor_media = 10
    aluno_menor = None
    for aluno in alunos:
        if aluno.get_media() < menor_media:
            menor_media = aluno.get_media()
            aluno_menor = aluno
    print(f"Menor média: {aluno_menor.get_nome()} com {menor_media:.2f}")
    
    # (d) Aprovação
    print("\n=== Situação dos alunos ===")
    for aluno in alunos:
        if aluno.aprovado() == True:
            status = "APROVADO"
        else:
            status = "REPROVADO"
        print(f"{aluno.get_nome()}: {aluno.get_media():.2f} - {status}")


# 4. Classe NumeroComplexo
class NumeroComplexo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario
    
    def __add__(self, outro):
        real_novo = self.real + outro.real
        imag_novo = self.imaginario + outro.imaginario
        return NumeroComplexo(real_novo, imag_novo)
    
    def __sub__(self, outro):
        real_novo = self.real - outro.real
        imag_novo = self.imaginario - outro.imaginario
        return NumeroComplexo(real_novo, imag_novo)
    
    def __mul__(self, outro):
        r = self.real * outro.real - self.imaginario * outro.imaginario
        i = self.real * outro.imaginario + self.imaginario * outro.real
        resultado = NumeroComplexo(r, i)
        return resultado
    
    def __str__(self):
        if self.imaginario >= 0:
            return f"{self.real} + {self.imaginario}i"
        else:
            return f"{self.real} - {abs(self.imaginario)}i"


# 5. Classe Horario
class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    
    def incrementar(self, segundos):
        total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo
        total_segundos = total_segundos + segundos
        self.hora = (total_segundos // 3600) % 24
        self.minuto = (total_segundos % 3600) // 60
        self.segundo = total_segundos % 60
    
    def diferenca(self, outro):
        total1 = self.hora * 3600 + self.minuto * 60 + self.segundo
        total2 = outro.hora * 3600 + outro.minuto * 60 + outro.segundo
        dif = total1 - total2
        if dif < 0:
            dif = dif * -1
        return dif
    
    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"


# 6. Classe Vetor3D
class Vetor3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def soma(self, outro):
        x_novo = self.x + outro.x
        y_novo = self.y + outro.y
        z_novo = self.z + outro.z
        return Vetor3D(x_novo, y_novo, z_novo)
    
    def subtracao(self, outro):
        x_novo = self.x - outro.x
        y_novo = self.y - outro.y
        z_novo = self.z - outro.z
        return Vetor3D(x_novo, y_novo, z_novo)
    
    def produto_escalar(self, outro):
        resultado = self.x * outro.x + self.y * outro.y + self.z * outro.z
        return resultado
    
    def produto_vetorial(self, outro):
        x = self.y * outro.z - self.z * outro.y
        y = self.z * outro.x - self.x * outro.z
        z = self.x * outro.y - self.y * outro.x
        vetor_resultado = Vetor3D(x, y, z)
        return vetor_resultado
    
    def modulo(self):
        resultado = (self.x**2 + self.y**2 + self.z**2)**0.5
        return resultado
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


# 7. Classe Carro
class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco
    
    def mostrar_preco(self):
        print(f"Preço: R$ {self.preco:.2f}")
    
    def exibir_dados(self):
        print(f"Marca: {self.marca}, Ano: {self.ano}, Preço: R$ {self.preco:.2f}")


def exercicio7():
    carros = []
    print("\n=== Exercício 7 ===")
    
    contador = 0
    while contador < 5:
        print(f"\nCarro {contador+1}:")
        marca = input("Marca: ")
        ano = int(input("Ano: "))
        preco = float(input("Preço: "))
        carro = Carro(marca, ano, preco)
        carros.append(carro)
        contador = contador + 1
    
    p = float(input("\nDigite o valor máximo para filtrar: "))
    print(f"\nCarros com preço menor que R$ {p:.2f}:")
    for carro in carros:
        if carro.preco < p:
            carro.exibir_dados()


# 8. Classe ContaCorrente
class ContaCorrente:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
    
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
    
    def deposito(self, valor):
        self.saldo = self.saldo + valor
        print(f"Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}")
    
    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            print(f"Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Saldo insuficiente!")


# 9. Classe Racional
class Racional:
    def __init__(self, p, q):
        if q == 0:
            raise ValueError("Denominador não pode ser zero!")
        self.p = p
        self.q = q
        self.simplificar()
    
    def simplificar(self):
        from math import gcd
        divisor = gcd(abs(self.p), abs(self.q))
        self.p = self.p // divisor
        self.q = self.q // divisor
        if self.q < 0:
            self.p = -self.p
            self.q = -self.q
    
    def inverter_sinal(self):
        novo_p = -self.p
        novo_q = self.q
        return Racional(novo_p, novo_q)
    
    def somar(self, outro):
        p = self.p * outro.q + outro.p * self.q
        q = self.q * outro.q
        resultado = Racional(p, q)
        return resultado
    
    def subtrair(self, outro):
        p = self.p * outro.q - outro.p * self.q
        q = self.q * outro.q
        resultado = Racional(p, q)
        return resultado
    
    def produto(self, outro):
        p_novo = self.p * outro.p
        q_novo = self.q * outro.q
        return Racional(p_novo, q_novo)
    
    def quociente(self, outro):
        if outro.p == 0:
            raise ValueError("Divisão por zero!")
        p_novo = self.p * outro.q
        q_novo = self.q * outro.p
        return Racional(p_novo, q_novo)
    
    def __str__(self):
        return f"{self.p}/{self.q}"


# Exemplos de uso
if __name__ == "__main__":
    print("Escolha o exercício para testar (1-9):")
    print("3 e 7 têm funções interativas específicas")
    
    # Exemplo Exercício 1
    print("\n=== Exemplo Exercício 1 ===")
    p = Pessoa("João", 30, "Rua A, 123")
    p.mostrar_endereco()
    p.alterar_endereco("Rua B, 456")
    p.mostrar_endereco()
    
    # Exemplo Exercício 4
    print("\n=== Exemplo Exercício 4 ===")
    c1 = NumeroComplexo(3, 2)
    c2 = NumeroComplexo(1, 7)
    soma = c1 + c2
    print(f"{c1} + {c2} = {soma}")
    produto = c1 * c2
    print(f"{c1} * {c2} = {produto}")
    
    # Exemplo Exercício 9
    print("\n=== Exemplo Exercício 9 ===")
    r1 = Racional(1, 2)
    r2 = Racional(1, 3)
    soma_r = r1.somar(r2)
    print(f"{r1} + {r2} = {soma_r}")
    prod_r = r1.produto(r2)
    print(f"{r1} * {r2} = {prod_r}")
    
    # Descomente para testar os exercícios interativos:
    # exercicio3()
    # exercicio7()