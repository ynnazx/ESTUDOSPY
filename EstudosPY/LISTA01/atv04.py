total = 0 #iniciando a variável total

for i in range(2):
    nota = float(input("Digite sua nota: "))
    total += nota #variavel acummulativa

media = total / 2

if media == 10:
    print("Aprovado com Distinção:", media)
elif media >= 7:
    print("Aprovado:", media)
else:
    print("Reprovado:", media)