from src.aula_01.Account import Account

def workspace():
	
	print("||||-------------- Digite suas informações abaixo --------------||||")
	
	name = str(input("Digite seu nome: "))
	account = int(input("Digite o número da sua conta: "))
	
	Account1 = Account(name, account, 0.0)
	
	print(Account1)

	deposit = float(input("Digite o valor do deposito: "))
	Account1.deposit(deposit)

	sake = float(input("Digite o valor do saque: "))
	Account1.withdraw(sake)

	print("Conta atualizada: ", Account1)

if __name__ == '__main__':

	workspace()
