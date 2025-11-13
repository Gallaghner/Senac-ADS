class Retangulo:
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura

    def calcula_area(self) -> float:
        return self.base * self.altura
    
r1 = Retangulo(12,24)
r2 = Retangulo(8,12)

x = r1.calcula_area()
y = r2.calcula_area()

print('Area: ',x)
print('Area: ',y)