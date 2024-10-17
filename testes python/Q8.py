#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês#
ValorHora = float(input("Qual valor que você ganha por hora trabalhada? ")) 
TempoMes = float(input("Quantas horas você trabalhou esse mês? "))
Pagamento = ValorHora*TempoMes
print(f"O valor a ser recebido por você é de {Pagamento}R$")