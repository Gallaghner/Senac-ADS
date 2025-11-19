# times = ["Palmeiras", "Flamengo", "São Paulo"]

# for i in range(len(times)):
#     print(f"{i + 1} - {times[i]}")

# n1 = int((input)("Digite um número inteiro: "))
# n2 = int((input)("Digite o segundo número inteiro: "))
# for i in range(n1+1, n2):
#     print(i)
#     s = sum(range(n1+1, n2))
# print(s)

# for i in range (1,21):
#     print(i)

# for i in range(1,21):
#     print(i, end=' ')

soma = 0
acumulador = 0
for i in range(5):
    num = int(input("Digite um número: "))
    soma = soma + num
    acumulador = acumulador + 1
media = soma / acumulador
print(media)
