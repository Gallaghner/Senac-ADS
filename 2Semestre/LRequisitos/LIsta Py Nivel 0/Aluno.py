class Aluno:
    def __init__(self,nome,ra,curso):
        self.nome = nome
        self.ra = ra
        self.curso = curso

    def mostrar_curso(self):
        print(f'O curso de {self.nome} é {self.curso}')

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso

a1 = Aluno('Joao', '6425', 'ADS')
a1.mostrar_curso()    
a1.alterar_curso('ENG')
a1.mostrar_curso()  

class Alunos:
    def __init__(self,nome,ra,n1,n2,n3):
        self.nome = nome
        self.ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    
    def mostrar_nome(self):
        print(f"Nome do aluno: {self.nome}")

    def calcular_media(self):
        self.media = ((self.n1 + self.n2 + self.n3) / 3)
        print(f"A média do aluno é: {self.media:.2f}")
        if self.media < 6:
            print('Aluno REPROVADO!')
        else:
            print("Aluno APROVADO!")

a1 = Alunos('Joao','034115',9,8,5)
a1.mostrar_nome()
a1.calcular_media()