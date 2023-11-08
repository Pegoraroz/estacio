peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
imc = peso / (altura * altura)
if imc <= 18.5:
    print(f"Seu imc é {imc}, você está abaixo do peso")
elif imc >= 18.6:
    print(f"Seu imc é {imc}, você está no peso ideal")
elif imc >= 25:
    print(f"Seu imc é {imc}, você está levemente acima do peso")
elif imc >= 30:
    print(f"Seu imc é {imc}, você está acima do peso")