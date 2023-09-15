lista = [4, 7, 13, 1, 15, 23, 9, 20]

soma = 0
for num in lista:
    if(num%2==0):
        soma=soma+num
print(f"A soma dos elementos pares da lista é: {soma}")