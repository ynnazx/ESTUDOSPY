#mesma coisa da atv02, alterando apenas o parametro do range para 3
numeros = [] 

for i in range(3):
    num = int(input("Digite um número: "))
    numeros.append(num) 

print("O maior número é:", max(numeros)) 