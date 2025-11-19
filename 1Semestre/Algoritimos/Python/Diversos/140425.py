# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))
# m  = (n1 + n2) /2
# print("A média é: ", m)
# if m >= 7 and m < 10:
#     print("Aprovado")
# elif m < 7:
#     print("Reprovado")
# elif m == 10:
#     print("Aprovado com distinção")

v = float(input("digite o valor da sua hora: "))
h = float(input("digite a quantidade de horas trabalhadas no mês: "))
sb =  v*h 
fgts = sb*0.11
if sb <= 900:
    ir1 = "0%"
    ir = 0
    inss = sb*0.10
    df = inss
    sf = sb - (sb*inss)
elif sb <= 1500:
    ir1 = "5%"
    ir = sb*0.05
    inss = sb*0.10
    df = inss + ir
    sf = sb - (inss + ir)
elif sb <= 2500:
    ir1 = "10%"
    ir = sb*0.10
    inss = sb*0.10
    df = inss + ir
    sf = sb - (inss + ir)
else:
    ir1 = "20%"
    ir = sb*0.10
    inss = sb*0.20
    df = inss + ir
    sf = sb - (inss + ir)
print("Salário bruto: (", v,"*",h,")     : R$", sb)
print(" (-) IR (", ir1,")     : R$", ir)
print(" (-) INSS (10%)     : R$", inss)
print("FGTS (11%)     : R$", fgts)
print("Total de descontos     : R$", df)
print("Salario Líquido     : R$", sf)




