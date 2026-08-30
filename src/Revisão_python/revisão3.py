## dicionarios, excessões

dicionario_teste = {"Victor Hugo" : 12345, "Junior": 6789, "Thiaguinho":1011}

## Método que retorna um objeto iteravel que consiste as chaves do dicionario

for key in dicionario_teste.keys():
    print(key, "->", dicionario_teste[key])

print(f"\n")

for key, keys in dicionario_teste.items():##Retorna tuplas como par de valores-chaves
    print(key, "->",keys)

print(f"\n")

##Troca de valor(dicionarios são mutaiveis)

dicionario_teste['Victor Hugo'] = 7890
print(dicionario_teste)

print(f"\n")

for key in sorted(dicionario_teste):##Dicionario ordenado
    print(f" ", key)

print(f"\n")


for key in dicionario_teste.values():##Funciona de forma semelhante a  keys, mas retorna valores.
    print(f" ", key)

print(f"\n")

##Adição de novo valor ao dicionario
dicionario_teste['Vaz'] = 12345
print(dicionario_teste)

## Ou usar uptade

dicionario_teste.update({'Neto': 3344})
print(dicionario_teste)

##Remover chave

print(f"\n")

del dicionario_teste['Vaz']
print(dicionario_teste)

print(f"\n")

## Remover o ultimo item

dicionario_teste.popitem()

print(dicionario_teste)
