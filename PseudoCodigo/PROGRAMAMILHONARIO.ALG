Algoritmo "ProgramaMilhonario"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 

var
 s, d, m: real


Inicio
 //Entrada

 escreva ("Digite o seu salario mensal: ")
 leia (s)
 escreva ("Digite quanto vc gasta de despesa: ")
 leia (d)

 //Processamento

 m := 1000000/((s - d)* 12)

 

 //Saida

 escreva ("Voce ficara milhonario : ", m," anos.")



Fimalgoritmo