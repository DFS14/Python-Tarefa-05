#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Lê o número de maçãs compradas
quantidadeMacas = int(input("Digite o número de maçãs compradas: "))


if quantidadeMacas < 12:
    precoUnitario = 1.30
else:
    precoUnitario = 1.00


custoTotal = quantidadeMacas * precoUnitario

print(f"O custo total da compra é R$ {custoTotal:.2f}")
