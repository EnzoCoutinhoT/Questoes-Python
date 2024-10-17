#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58#
altura = float(input("Qual a sua altura em centimetros? "))
ideal = (72.7*altura)-58
print(f"Com a altura de:{altura} metros, o seu peso ideal é {ideal:.2f} Kg") 