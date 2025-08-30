print("Operação - Adição!")

while True:
    num01 = int(input("Digite um número: "))
    num02 = int(input("Digite um número: "))
    resultado = num01 + num02
    print(f"{num01} + {num02} = {resultado}")

    resposta = input("Deseja realizar mais uma soma? [S ou N]: ").lower()
    if resposta != "s":
        print("Operação finalizada.")
        break