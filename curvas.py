from math import sqrt

ray = float(input("Insira o raio da curva: "))
coeficiente_de_atrito = 0.8
gravidade = 10
multiplies_variables = ray*coeficiente_de_atrito*gravidade
velocidade_maxima = sqrt(multiplies_variables)
# Arredonda 2 casas
velocidade_maxima = round(velocidade_maxima, 2)
# Converte para km/h
velocidade_maxima = velocidade_maxima*3.6
print("km/h",velocidade_maxima)
