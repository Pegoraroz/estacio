numero = int(input("Fatorial de: ") )

resultado=1
contagem=1

while contagem <= numero:
    resultado *= contagem
    contagem += 1

print(resultado)