#Calculadora de Compras
unidade = 10

compra = int(input("Insira a quantidade de itens comprados: "))
if (compra <= 10):
    total = (unidade * compra)
    print(f"Seu total é de: {total}")
elif (compra >= 11):
    total = ((unidade * compra) * 0.9)
    print(f"Você recebeu um desconto de 10%, o valor total é: {total}")
elif (compra >= 20):
    total = ((unidade * compra) * 0.8)
    print(f"Você recebeu um desconto de 20%, o valor total é: {total}")