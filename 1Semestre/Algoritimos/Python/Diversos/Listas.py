# list / len / type / extend / pop

lista1 = [1,2,3,4,5]
lista2 = ["Ederson", "João", "Pedro", "Maria"]
print(lista1) # Imprime a lista inteira
print(type(lista1)) # Imprime o tipo da variável

lista1 = ["João", 1.0, 5, [10, 20]]
print(lista1)
print(len(lista1)) # Imprime o tamanho da lista

lista = [1,2,3]
lista.extend([4,5,6])
print(lista) # Adiciona os elementos da segunda lista na primeira


# O `elif` é usado para verificar condições adicionais caso a condição do `if` seja falsa.
# Ele funciona como um "senão, se". Você pode usar vários `elif` para testar múltiplas condições.
# Se a condição do `if` for verdadeira, o bloco do `elif` será ignorado.
# Se nenhuma condição for verdadeira, o bloco do `else` será executado.
# Elif
idade = int(input("Digite sua idade: "))
if idade >= 16 and idade < 18:
    print("Pode votar")
elif idade <16:                 
    print("Apenas estude")  
else: 
    print("Pode dirigir")    




