while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    print("Nome deve ter mais de 3 caracteres.")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break
        print("Idade deve estar entre 0 e 150.")
    except ValueError:
        print("Digite um número inteiro válido para a idade.")

while True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario > 0:
            break
        print("Salário deve ser maior que zero.")
    except ValueError:
        print("Digite um valor numérico válido para o salário.")

sexos_validos = ["M", "F"]
while True:
    sexo = input("Digite seu sexo (M/F): ").upper()
    if sexo in sexos_validos:
        break
    print("Sexo deve ser 'M' ou 'F'.")

estados_civis_validos = ["S", "C", "V", "D"]
while True:
    estado_civil = input("Digite seu estado civil (S/C/V/D): ").upper()
    if estado_civil in estados_civis_validos:
        break
    print("Estado civil deve ser 'S', 'C', 'V' ou 'D'.")

print("\nDados cadastrados com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")