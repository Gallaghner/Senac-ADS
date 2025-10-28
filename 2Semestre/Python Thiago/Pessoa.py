class Pessoa:
    def __init__(self,nome,fone,email,cidade,estado):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.cidade = cidade
        self.estado = estado


    def get_all(self):
        print(self.nome)
        print(self.fone)
        print(self.email)
        print(self.cidade)
        print(self.estado)

p1 = Pessoa('João','67998654823','jprodriguespro@gmail.com','Campo Grande', 'MS')

p1.get_all()