
#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Conversão de Temperatura

#Celsius para Fahrenheit

temperaturaFahrenheit = int (input("Digite a temperatura em graus Celsius: "))
temperaturaFahrenheit = (temperaturaFahrenheit * 9/5) + 32
print("A temperatura em Fahrenheit é: ", temperaturaFahrenheit, "°F")

temperaturaCelsius = int (input("Digite a temperatura em graus Fahrenheit: "))
temperaturaCelsius = (temperaturaCelsius - 32) * 5/9
print("A temperatura em Fahrenheit é: ", temperaturaCelsius, "°C")
