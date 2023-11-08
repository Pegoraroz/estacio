#Sistema de validação de nota

nota = int(input("Digite sua nota: "))

if (nota >= 7):
    print("Você foi aprovado!")
elif (nota >= 5):
    print("Você está em recuperação")
elif (nota <= 5):
    print("Você foi reprovado")