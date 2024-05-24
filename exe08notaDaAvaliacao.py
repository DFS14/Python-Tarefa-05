#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Lê as notas da 1a. e 2a. avaliações do aluno

nota1 = float(input("Digite a nota da 1a. avaliação: "))
nota2 = float(input("Digite a nota da 2a. avaliação: "))


media = (nota1 + nota2) / 2

if media >= 6:
    print(f"Aluno APROVADO! Média: {media:.2f}")
else:
    print(f"Aluno REPROVADO! Média: {media:.2f}")
