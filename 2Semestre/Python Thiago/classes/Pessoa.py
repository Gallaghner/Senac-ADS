class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def mostrar_nome(self):
        return self.nome
    
    def alterar_idade(self, nova_idade):
        self.idade = nova_idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, endereco, matricula, curso):
        super().__init__(nome, idade, endereco)
        self.matricula = matricula
        self.curso = curso
    
    def mostrar_info(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Curso: {self.curso}"
    
    def alterar_curso(self, novo_curso):
        self.curso = novo_curso


# Testando
p1 = Pessoa("Bonassa", 25, "Rua A")
p1.mostrar_nome()

a1 = Aluno("João", 20, "Rua B", "2024001", "Ciência da Computação")
print(a1.mostrar_info())
print(a1.mostrar_nome())  # Herdado de Pessoa
a1.alterar_curso("Engenharia")
print(a1.mostrar_info())