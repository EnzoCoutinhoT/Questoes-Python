#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit. C = (5 * (F-32) / 9).#
Celsius = float(input("Qual valor da temperatura em Celsius? "))
Farenheit = (Celsius*1.8) + 32
print(f"{Celsius} graus  Celsius correspondem a {Farenheit:.2f} graus Farenheit")
