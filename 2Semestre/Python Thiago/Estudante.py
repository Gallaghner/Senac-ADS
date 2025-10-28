class Estudante: 
    def __init__(self,nome,idade,nota): ## METODO CONSTRUTOR
        self.nome = nome   ### ATRIBUTO
        self.idade = idade  ###ATRIBUTO
        self.nota = nota    ###ATRIBUTO

    def get_grade(self):
        print(self.nota)


e1 = Estudante("Luis",20,10)
e2 = Estudante("Jow",22,10)

def get_grade(self):
    print(self.nota)

e1.get_grade()