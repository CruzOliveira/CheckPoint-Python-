#Exercicio9

a=int(input("Digite o numero de votos para o candidato A:"))
b=int(input("Digite o numero de votos para o candidato B:"))
c=int(input("Digite o numero de votos para o candidato C:"))
nulo=int(input("Digite o numero de votos nulos:"))
branco=int(input("Digite o numero de votos em branco:"))

total= a + b + c + nulo + branco
p_a= a * 100 / total
p_b= b * 100 / total
p_c= c * 100 / total
p_n= nulo * 100 / total
p_br= branco * 100 / total

print("O precentual do eleitor: ", p_a," %")
print("O precentual do eleitor: ", p_b," %")
print("O precentual do eleitor: ", p_c," %")
print("O precentual de votos nulos: ", p_n," %")
print("O precentual de votos em branco: ", p_br," %")

