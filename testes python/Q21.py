#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, genero Inválido.
genero = str(input("Qual o seu gênero? F ou M?"))
if genero =="M":
    print("Masculino")
elif genero =="F":
    print("Feminino")