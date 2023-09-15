lista = [4, 7, 13, 1, 15, 23, 9, 20]

n=len(lista)
soma=0
for i in range(n):
    if(lista[i]%2==0):
        soma=soma+lista[i]
print(f"A soma dos elementos pares da lista é: {soma}")