from src.Student.Student import Student


def workspace():


    print("====Digite as informações do estudante====")


name = str(input("Informe o nome do estudante: "))
age = int(input("Informe a idade do estudante:"))
note = 0
faltas = 0

Student(name, age, note, faltas)

n = input(int("Informe a quantidade de notas do estudante: "))

print("\n=======Informações do Estudante=======\n")

if __name__ == '__main__':
    workspace()
