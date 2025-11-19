# Manipulação de strings em Python
# capitalize / casefold / upper / lower / isupper / islower / isdigit / replace / split / find / len / in / substring / slice

a = "EDERSON"
print(a.isupper())  # Verifica se todos os caracteres estão em maiúsculas
a = "ederson"
print(a.islower())  # Verifica se todos os caracteres estão em minúsculas

a = "Ederson"
print(a.capitalize())  # Converte o primeiro caractere para maiúscula e o restante para minúscula
a = "Ederson"
print(a.casefold())  # Converte todos os caracteres para minúsculas, mais agressivo que lower()

a = "Ederson"
print(a.upper())  # Converte todos os caracteres para maiúsculas
a = "Ederson"
print(a.lower())  # Converte todos os caracteres para minúsculas

b = "1234"
print(b.isdigit())  # Verifica se todos os caracteres são dígitos

a = "João Paulo"
print(a.replace("Paulo", "Pedro"))  # Substitui todas as ocorrências de "Paulo" por "Pedro"

a = "João Paulo"
index = a.find("Paulo")
print(index)  # Encontra a posição da primeira ocorrência de "Paulo"
index = a.find("Pedro")
print(index)  # Tenta encontrar "Pedro", mas retorna -1 porque não está presente

a = "João Paulo"
print("Paulo" in a) # Verifica se "Paulo" está presente em "João Paulo"

a = "João Paulo"
print(a.count("a")) # Conta quantas vezes a letra "a" aparece

s = "Olá, mundo!"
print(s[2]) # Acessa o caractere na posição 2

s = "Olá, mundo!"
print(s[2:7]) # Acessa os caracteres nas posições 2 a 6

s = "Olá, mundo!"
print(s[2:]) # Acessa os caracteres a partir da posição 2

s = "Olá, mundo!"
print(s[:7]) # Acessa os caracteres até a posição 6
