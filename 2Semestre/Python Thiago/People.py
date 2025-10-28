
class People: ##SUPERCLASSSS HERANÇA
    def __init__(self,nome,email,senha):
        self.name = nome
        self.mail = email
        self.password = senha

    def hello(self):
        print(f'Hellooooooo {self.name}')

class Student(People):
    def _init_(self,nome,email,senha,ra):
        super().__init__(nome,email,senha)
        self.ra = ra

p1 = People('Joao','joao@gmail.com','79273')
p1.hello()

p2 = Student('Joao','joao@gmail.com','92737','213237')
p2.hello()