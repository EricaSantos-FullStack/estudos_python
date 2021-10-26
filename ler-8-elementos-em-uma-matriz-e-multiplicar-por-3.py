#ler-8-elementos-em-uma-matriz-e-multiplicar-por-3

vetorA = [1,1,1,1]
vetorB = [1,1,1,1]

for x in range(0, 4, 1):
  vetorA[x] = int(input("Digite um número: "))
  vetorB[x] = vetorA[x] * 3 

for x in range(0, 4, 1):
  print(f'Indice {x} -> vetorA = {vetorA[x]} = vetorB ={vetorB[x]}')
