numeros = []

n = int(input("Quantos números você deseja inserir? "))

for i in range(n):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")