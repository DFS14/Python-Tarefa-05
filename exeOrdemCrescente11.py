#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Escrever os valores em ordem crescente


valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))


valor_min = min(valor1, valor2)
valor_max = max(valor1, valor2)


print(f"Valores em ordem crescente: {valor_min}, {valor_max}")
