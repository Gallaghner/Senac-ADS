#n1 = int(input("Digite o primeiro número: "))
#n2 = int(input("Digite o segundo número: "))

#if n1 > n2 : 
#    print(n1)
#else :
#    print(n2)                                           #exibe o maior número


# n = int(input("Digite um número: "))
# if n > 0:
#     print("O número é positivo")
# elif n < 0:
#     print("O número é negativo")             #informa se o número é positivo ou negativo ou netro
# elif n == 0:
#     print("O número é neutro")


# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))

# m = n1 + n2 / 2
# print("A média é:", m)
# if m >= 6:
#     print("Aprovado")
# else:
#     print("Reprovado")                     #informa se o aluno foi aprovado ou reprovado


# s = float(input("Digite o salário: "))
# if s < 500:
#     a = s * 0.15
#     print("O novo salário é:", s + a)
# elif s >= 500 and s < 1000:
#     a = s * 0.10
#     print("O novo salário é:", s + a)
# elif s > 1000:
#     a = s * 0.05
#     print("O novo salário é:", s + a)    #informa o novo salário de acordo com o aumento                         

# s = input("Digite o sexo (M/F/O): ").upper()
# if s == "M":
#     print("Masculino")
# elif s == "F":
#     print("Feminino")
# elif s == "O":
#     print("Outro")
# else:
#     print("Sexo inválido")            #informa o sexo de acordo com a letra digitada

# l = input("Digite uma letra: ").upper()
# if l == "A" or l == "E" or l == "I" or l == "O" or l == "U":
#     print("A letra é uma vogal")

# else:
#     print("A letra é uma consoante")                 #informa se a letra digitada é uma vogal ou consoante

# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# n3 = int(input("Digite o terceiro número: "))
# if n1 > n2 and n1 > n3:
#     print("O maior número é: ", n1)
# elif n2 > n1 and n2 > n3:
#     print("O maior número é: ", n2)
# elif n3 > n1 and n3 > n2:
#     print("O maior número é: ", n3)
# if n1 < n2 and n1 < n3:
#     print("O menor número é: ", n1)
# elif n2 < n1 and n2 < n3:
#     print("O menor número é: ", n2)
# elif n3 < n1 and n3 < n2:
#     print("O menor número é: ", n3)
# else:
#     print("Os números são iguais")       #informa o maior e o menor número digitado

# p1 = float(input("inofrme o valor do primeiro produto: "))
# p2 = float(input("Informe o valor do segundo produto: "))
# p3 = float(input("informe o valor do terceiro produto: "))
# if p1 < p2 and p1 < p3:
#     print("Compre o primeiro produto, pois é o mais barato.")
# elif p2 < p1 and p2 < p3:
#     print("Compre o segundo produto, pois é o mais barato.")
# elif p3 < p1 and p3 < p2:
#     print("Compre o terceiro produto, pois é o mais barato.")
# if p1 == p2 and p2 == p3:
#     print("Os três produtos tem o mesmo valor.")     #informa o produto mais barato ou se possuem o mesmo valor

# num_1 = float(input("Digite o primeiro número: "))
# num_2 = float(input("Digite o segundo número: "))
# num_3 = float(input("Digite o terceiro número: "))

# if num_1 > num_2 and num_2 > num_3:
#     print(num_1, ",", num_2, ",", num_3)
# elif num_1 > num_3 and num_3 > num_2:
#     print(num_1, ",", num_3, ",", num_2)
# elif num_2 > num_1 and num_1 > num_3:
#     print(num_2, ",", num_1, ",", num_3)
# elif num_2 > num_3 and num_3 > num_1:
#     print(num_2, ",", num_3, ",", num_1)
# elif num_3 > num_1 and num_1 > num_2:
#     print(num_3, ",", num_1, ",", num_2)d        
# elif num_3 > num_2 and num_2 > num_1:
#     print(num_3, ",", num_2, ",", num_1)


s = float(input("Digite o salário: "))
if s <= 280.55:
    p = 22.51
    r = s*(22.51/100)
    sf = s*(22.51/100) + s
elif s >= 280.56 and s < 709.72:
    p = 15.39
    r = s*(15.39/100)
    sf = s*(15.39/100) + s
elif s >= 709.73 and s < 1501.33:
    p = 10.97
    r = s*(10.97/100) 
    sf = s*(10.97/100) + s
elif s >= 1501.34:
    p = 5.19
    r = s*(5.19/100) 
    sf = s*(5.19/100) + s
print("O salário inicial era de ", s,", após o reajuste de ", p,"% que daria R$", r," a mais. O salário final ficaria R$", sf)










                                        


                                                   