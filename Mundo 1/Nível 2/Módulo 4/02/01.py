def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo):
            minimo = elem
    return minimo

lista_teste = [10, 14, 28, 7, 23, 14, 4]
menor = encontrar_minimo(lista_teste)
print(f"O menor elemento da lista é:[{menor}]")