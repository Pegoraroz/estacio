import copy

lista1 = [[1,2,3], [4,5,6], [7,8,9]]

lista2 = copy.deepcopy(lista1)

#lista1[2][2] = 11
lista1.append([10, 10, 10])

print("Lista 1: ", lista1)
print("Lista 2: ", lista2)