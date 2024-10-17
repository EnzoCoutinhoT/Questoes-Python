#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.#

PesoPeixe = int(input("Qual valor do peso dos peixes? "))
Excedente = PesoPeixe-50
ValorExcedente = Excedente*4
if PesoPeixe>50:
    print(f"O valor exdeceu em:{Excedente:.2f} e você precisa pagar uma multa de {ValorExcedente:.2f}")
elif PesoPeixe>=0&PesoPeixe<=50:
    print("O valor não excedeu")
elif PesoPeixe<0:
    print("Não digite valores negativos")
