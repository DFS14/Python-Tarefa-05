
#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Percentual de Votos


totalEleitores = int(input("Digite o número total de Eleitores: "))
votosBrancos = int (input("Digite o número total de Voto Brancos: "))
votosNulos = int(input("Digite o número total de Voto Nulos: "))
votosValidos = int(input("Digite o número total de Voto válidos: "))

percentualVotosBrancos = (votosBrancos/totalEleitores )*100
percentualVotosNulos = (votosNulos/totalEleitores )*100
percentualVotosValidos = (votosValidos/totalEleitores )*100

print(f"Percentual de votos brancos: {percentualVotosBrancos:.2f} %")
print(f"Percentual de votos nulos: {percentualVotosNulos:.2f} %")
print(f"Percentual de votos válidos: {percentualVotosValidos:.2f} %")