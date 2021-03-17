Algoritmo "ProgramaPrestacao"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 

Var
N, B, J, D: real


Inicio

 //Entrada
 escreva ("Digite qual e o valor do boleto:R$ ")
 leia (B)
 escreva ("Digite o valor do juros: ")
 leia (J)
 escreva ("Digite quantos dias de atraso: ")
 leia (D)
 
 //Processamento
N:= B + ( B *( J / 100 )) * D

 //Saida
 escreva ("O novo boleto emitido sera de:R$", N)

Fimalgoritmo