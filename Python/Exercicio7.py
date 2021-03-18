#Exercicio7

b=float(input("Digite o valor do boleto:"))
j=float(input("Digite o valor do juros:"))
dia=float(input("Digite o dia de atraso:"))

n= b + (b * ( j / 100 )) * dia

print("O novo valor do boleto sera de: ", n)
