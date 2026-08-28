## dicionarios, excessões

dicionario_teste = {"Victor Hugo": 5566, "Famoso": 8899}
empty_dicionario = {}

print(dicionario_teste)
print(empty_dicionario)

for i in dicionario_teste:
    if("Victor Hugo" in i):
        print(f"{i} está na lista!")
    else:
        print(f"{i} não está!")
