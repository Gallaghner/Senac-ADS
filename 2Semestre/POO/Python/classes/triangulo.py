
class Triangulo:
    def __init__(self,base:int,altura:int):
        self.__base = base
        self.__altura = altura

    def calcula_area(self) -> float:
        area = (self.base * self.altura) / 2
        return area
    
    def get_base(self):
        return self.__base
    

t1 = Triangulo(9,12)
t2 = Triangulo(4.5, 6)

# x = t1.get_base()
# print("Base: ",x)
