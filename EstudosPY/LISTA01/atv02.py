numeros = [] #array vazio que armazenará os números

for i in range(2):
    num = int(input("Digite um número: "))
    numeros.append(num) #adiciona o num no array

print("O maior número é:", max(numeros)) #retorna automaticamente o maior número do array

"""
SEM O FOR E O ARRAY >>>>

num01 = int(input("Digite um número: "))
num02 = int(input("Digite um número: "))

if num01 > num02:
    print("O maior número é:", num01)
else:
    print("O maior número é:", num02)

"""