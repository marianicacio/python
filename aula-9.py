#importando biblioteca randômica
import random

#definir o tamanho da matriz
TAM = 3

#definido um laço para a matriz que
#intera TAM vezes
mat1 = [[] for _ in range(TAM)]
mat2 = [[] for _ in range(TAM)]
mat3 = [[0 for _ in range(TAM)] for _ in range(TAM)]

#Função soma
def soma():
    for lin in range(TAM):
        for col in range(TAM):
           mat3[lin][col] = mat1[lin][col] + mat2[lin][col]

#preenchendo a matriz com numeros aleatorios
for lin in range(TAM):
    for col in range(TAM):
        mat1[lin].append(random.randrange(0,10))
        mat2[lin].append(random.randrange(0,10))
#para exibir 
print("Matriz 1: ")
for linha in mat1:
    print(linha)

print("Matriz 2: ")
for linha in mat2:
    print(linha)

print("Matriz 3: ")
soma()
for cont in mat3:
    print(cont)
