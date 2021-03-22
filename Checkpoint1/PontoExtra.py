#Exercicio

nome=(input("Digite o seu nome:" ))
sal=float(input("Digite o seu salario fixo mensal: R$" ))
vf=float(input("Digite o total vendido no setor feminino: R$" ))
vm=float(input("Digite o total vendido no setor masculino: R$" ))
vi=float(input("Digite o total vendido no setor infantil: R$" ))
vb=float(input("Digite o total vendido no setor deleza: R$" ))

cf= vf * 2 / 100
cm= vm * 2 /100
ci= vi * 4 /100
cb= vb * 6 /100

comi= cf + cm + ci + cb
total= comi + sal
 
print("Prezaado(a): ", nome)
print("Seu salário fixo é de", sal," reais e sua comissão referente o mês vigente foi calculado em", comi," reais.")
print("Total a receber:", total,"reais.")