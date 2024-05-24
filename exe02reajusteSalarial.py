#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Reajuste Salarial

salarioAtual = float (input("Digite o salário Atual: "))
percentualDeReajuste = float(input("Digite o percentual de reajuste: "))

novoSalario = salarioAtual*(1 + percentualDeReajuste/100)
print(f"Novo salário:R$ {novoSalario:.2f}")
