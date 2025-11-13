# #1 contando números
# for n in range(1,11):
#     print(n)

#2 lista de frutas
# frutas = ('Maçã', 'Banana', 'Melão', 'Abacaxi', 'Melancia')
# for fruta in frutas:
#     print(f"Eu gosto de {fruta}")

# #3 somando valores 
# numeros = (5,2,9,10)
# soma = 0

# for n in numeros:
#     soma += n
# print(soma)

# #4 contando letras
# palavra = input("Digite uma palavra: ")
# nletras = 0

# for letra in palavra: 
#     nletras += 1
# print(nletras)

# #5 separando pares e ímpares:
# numeros = (1,2,3,4,5,6,7,8,9,10)

# for n in numeros:
#     if n %2 == 0:
#         print(f'{n} é par')
#     else: 
#         print(f'{n} é impar')

# ============================================= Intermediário =============================================

# #1 Multipicação mágica

# numero = int(input('Digite um número: ')) #tive que especificar que é um int pro range funcionar
# x = 1
# for n in range(numero):  #porque eu tive que mudar pra range pra funcionar ao invés de chamar só for n in numero???
#     print(f'{numero} = {numero*x}')
#     x += 1

#2 contando doces
doces = [5,3,9,7,2,1]
total = 0
mais_de_5 = 0

for t in doces:
    total += t
    if t > 5:
        mais_de_5 += 1

print(f'O total de doces ganhos foi de: {total}')
print(f'{mais_de_5} crianças garanharam mais de 5 doces')
