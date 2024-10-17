#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).#
Temperatura = float(input("Qual valor da temperatura em Farenheit? "))
Celsius = (5*(Temperatura-32))/9
print(f"{Temperatura} em Farenhent correspondem a {Celsius:.2f} graus Celsius")