with open("Cadastro.txt", "a") as x:
            x.write("Cadastro\n")

with open("Cadastro.txt", "r", encoding="utf-8") as f:
     for linha in f:
         if "joão" in linha.lower():
             print(linha)


with open"Cadastro.txt", r) as f:
linhas = f.readlines()

("terceira linha")