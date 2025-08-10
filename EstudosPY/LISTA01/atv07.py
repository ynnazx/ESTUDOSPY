print("Responda as perguntas para a invetigação do crime. (s/n)")

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas_sim = 0

for pergunta in perguntas: #percorre o array exibindo cada pergunta
    resposta = input(pergunta + " (s/n): ").lower() #armazena a resposta do usuário
    if resposta == 's': #condiciona a resposta do usuário 
        respostas_sim += 1

if respostas_sim == 2:
    print("Suspeito")
elif respostas_sim == 3 or respostas_sim == 4:
    print("Cúmplice")
elif respostas_sim == 5:
    print("Assassino")
else:
    print("Inocente")