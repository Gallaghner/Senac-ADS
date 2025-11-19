class Aluno:  
    def __init__(self, nome, ra, n1, n2, n3):
        self.nome = nome
        self.ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def calcular_media(self):
        self.media = (self.n1 + self.n2 + self.n3) / 3

# lista que vai armazenar OBJETOS Aluno (não só o RA!)
dados_alunos = []

for i in range(5):
    print(f"\n--- Aluno {i+1} ---")
    ra = input("RA: ")
    nome = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    aluno = Aluno(nome, ra, n1, n2, n3)
    dados_alunos.append(aluno)  # adiciona o OBJETO, não apenas o RA

maior_media = -1
menor_media = 11
aluno_maior = None
aluno_menor = None

for aluno in dados_alunos:
    media = Aluno.calcular_media()

    if media > maior_media:
        menor_media = media
        aluno_maior = aluno

    if media < menor_media:
        menor_media = media
        aluno_menor = aluno

print("\n === RESULTADOS === ")
for Aluno in dados_alunos:
    media = aluno.calcular_media()
    status = 'APROVADO' if media >=6 else "REPROVADO"
    print(f"{aluno.nome} - Média: {media:.2f} - {status}")

print("\nAluno com MAIOR média:")
print(f"{aluno_maior.nome} - Média: {maior_media:.2f}")

print("\nAluno com MENOR média:")
print(f"{aluno_menor.nome} - Média: {menor_media:.2f}")