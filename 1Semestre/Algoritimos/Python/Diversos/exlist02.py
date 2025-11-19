listas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(listas[1:9])
print(listas[8:10])

print("Os númeos pares são:", listas[2:11:2]) # Imprime os números pares
print("Os números ímpares são:", listas[0:11:3]) # Imprime os números ímpares

listas.sort(reverse = True) # Ordena a lista em ordem decrescente
print(listas)

p1 = [7.0, 8.3, 10.0, 6.5, 9.3]
p2 = [8.5, 6.9, 5.0, 7.5, 9.8]

mediap1 = sum(p1)/len(p1)
print(f"A média da prova 1 é: {mediap1:.2f}")

mediap2 = sum(p2)/len(p2)
print(f"A média da prova 2 é: {mediap2:.2f}")
print(f"{mediap2:.2f}")
