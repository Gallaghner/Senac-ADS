n = [1, 2, 3 , 4]
maior_número = max(n) # Retorna o maior número da lista
print("O maior número é:", maior_número)
menor_número = min(n ) # Retorna o menor número da lista
print("O menor número é:", menor_número)
quantidade = len(n) # Retorna a quantidade de elementos da lista
print("A quantidade de elementos é:", quantidade)
soma = sum(n ) # Retorna a soma dos elementos da lista
print("A soma dos elementos é:", soma)

l = [1, 1, 2, 3, 4, 5]
n1 = l.count(1) # Conta quantas vezes o número 1 aparece na lista
print("O número 1 aparece", n1, "vezes") 

l = [1, 2, 3, 4, 5]
print(l)
l[2] = "laranja"
print(l) # Substitui o elemento da posição 2 por "laranja"

l = [[1,2], [3,4], [5,6]]
print(sum(l[0])+sum(l[1])+sum(l[2])) # Soma todos os elementos da lista

l = [1,2,3]
x = sum(l[0:1])
y = sum(l[0:2])
z = sum(l[0:3])
print(x, y, z)
print([l[0], l[0]+l[1], l[0]+l[1]+l[2]]) # Outra forma de fazer a mesma coisa

l = [1,2,3,4]
l.pop(0)
l.pop(2)
print(l) # Remove o elemento da posição 0 e o da posição 2

l = [1,2,3,4]
print(l[1:3]) # Imprime os elementos da posição 1 até a posição 3

lista = ["Alemanha", "Itália", "Japão"]

# Adiciona todos os países da América do Sul
lista.extend(["Brasil", "Argentina", "Uruguai", "Paraguai", "Chile", "Colômbia", "Venezuela", "Equador", "Peru", "Bolívia", "Guiana", "Suriname"])

# Adiciona todos os países da América do Norte
lista.extend(["Estados Unidos", "Canadá", "México"])

# Adiciona todos os países da América Central
lista.extend(["Guatemala", "Honduras", "El Salvador", "Nicarágua", "Costa Rica", "Panamá", "Belize"])

# Adiciona as capitais de todos os países adicionados
capitais = [
    "Brasília", "Buenos Aires", "Montevidéu", "Assunção", "Santiago", "Bogotá", "Caracas", "Quito", "Lima", "Sucre",
    "Georgetown", "Paramaribo", "Ottawa", "Washington, D.C.", "Cidade do México", "Cidade da Guatemala", "Tegucigalpa",
    "San Salvador", "Manágua", "San José", "Cidade do Panamá", "Belmopan"
]
lista.extend(capitais)

print(lista)