#importando biblioteca randômica
import random

#definir o tamanho da matriz
TAM = 100

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

#Função de subtração
def sub():
    for lin in range(TAM):
        for col in range(TAM):
           mat3[lin][col] = mat1[lin][col] - mat2[lin][col]

#Função de multiplicação
def mult():
    for lin in range(TAM):
        for col in range(TAM):
           mat3[lin][col] = mat1[lin][col] * mat2[lin][col]

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

resp = input("Escolha a operação: +")

print("Matriz Soma ")
soma()
for cont in mat3:
    print(cont)

print("Matriz Subtração ")
sub()
for cont in mat3:
    print(cont)

print("Matriz Multiplicação")
mult()
for cont in mat3:
    print(cont)
