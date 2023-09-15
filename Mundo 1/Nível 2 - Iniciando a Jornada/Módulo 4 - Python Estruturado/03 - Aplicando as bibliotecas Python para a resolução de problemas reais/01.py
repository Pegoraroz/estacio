import numpy as np

def entrada():
    coeficiente = quantidade = eval(input("Digite o valor do coeficiente: "))
    return coeficiente

def calc_delta(a,b,c):
    delta = b*b-4*a*c
    return delta

def calc_raiz(a,b,c,delta):
    if(delta<0):
        resultado = "A equação não possui raízes nos números reais"
    elif(delta==0):
        x=-b/(2*a)
        resultado = f"A equação possui apenas uma raiz real: {x}"
    else:
        x1=(-b-np.sqrt(delta))/(2*a)
        x2=(-b+np.sqrt(delta))/(2*a)
        resultado = f"A equação possui duas raízes reais: {x1} e {x2}"
    return resultado

a = entrada()
b = entrada()
c = entrada()

delta=calc_delta(a,b,c)

resultado=calc_raiz(a,b,c,delta)
print(resultado)