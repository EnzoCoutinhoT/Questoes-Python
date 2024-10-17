#Faça um Programa que leia três números e mostre o maior deles.#
n1 = int(input("Qual o n1 "))
n2 = int(input("Qual o n2 "))
n3 = int(input("Qual o n3 "))
if n1>n2 and n1>n3:
    print(f"O maior número é {n1}")
elif n2>n1 and n2>n3:
    print(f"O maior número é {n2}")
elif n3>n1 and n3>n2:
    print(f"O maior número é {n3}")
elif n3==n2 and n3==n1:
    print("Todos os números são iguais")
