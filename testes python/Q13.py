#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,#
# utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7#
altura = float(input("Qual é a sua altura em metros? "))
genero = str(input("Qual é o seu gênero? "))
idealmulher = (altura*62.1)-44.7
idealhomem = (altura*72.2)-58
if(genero=="Masculino"or genero=="Homem"):
    print(f"O seu peso ideal para sua altura é: {idealhomem:.2f}")
elif(genero=="Feminino" or genero=="Mulher"):
    print(f"O seu peso ideal para a sua altura é {idealmulher:.2f}")