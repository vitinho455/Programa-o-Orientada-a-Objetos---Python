##### Revisão de Listas


qtde = int(input("Digite a quantidade de elementos que deseja colocar na lista: "))

my_list = []

for i in range(qtde):

    element = int(input(f"Digite o {i+1}° elemento: "))
    if(element == 0):
        while(element == 0):
            element = int(input("Digite outro elemento: "))
    my_list.append(element)

    my_list.sort(); ## Classificar a lista
    my_list.reverse(); ## Inverte a lista

print("Elementos presentes: ", my_list)

print("Uma parte da lista: ", my_list[1:4])## Retorna uma parte da lista
del my_list[2:4] ## Exclusão de uma parte da lista
print("Exclusão de uma parte da lista: ", my_list)

print(5 in my_list) ## verifica se um determinado elemento (seu argumento à esquerda) está atualmente armazenado em algum lugar dentro da lista
print(4 not in my_list)
print(5 not in my_list) ## verifica se um determinado elemento (seu argumento à esquerda) está ausente em uma lista

