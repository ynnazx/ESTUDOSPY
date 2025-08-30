numeros = []

n = int(input("Quantos números você deseja inserir? "))

for i in range(n):
    while True:
        num = float(input(f"Digite o {i+1}º número (entre 0 e 1000): "))
        if 0 <= num <= 1000:
            numeros.append(num)
            break
        else:
            print("Valor inválido! Digite um número entre 0 e 1000.")

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")