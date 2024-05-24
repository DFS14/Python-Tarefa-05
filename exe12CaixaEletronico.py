#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Calcular o saldo atual e verificar se é positivo ou negativo

numero_conta = input("Digite o número da conta do cliente: ")
saldo = float(input("Digite o saldo: "))
debito = float(input("Digite o débito: "))
credito = float(input("Digite o crédito: "))


saldo_atual = saldo - debito + credito


if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")


print(f"Saldo Atual: R$ {saldo_atual:.2f}")
