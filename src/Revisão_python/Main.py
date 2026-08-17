qtde = int(input("Digite a quantidade de elementos que deseja colocar na lista: "))

my_list = []

for i in range(qtde):

    element = int(input(f"Digite o {i+1}° elemento: "))
    if(element == 0):
        while(element == 0):
            element = int(input("Digite outro elemento: "))
    my_list.append(element)

print("Elementos presentes: ", my_list)

#################################################


