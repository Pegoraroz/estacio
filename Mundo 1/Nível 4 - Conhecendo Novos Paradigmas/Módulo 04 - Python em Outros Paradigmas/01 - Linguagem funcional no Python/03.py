veiculos = ['aviao', 'carro', 'navio', 'onibus']

f_maiuscula = lambda x: str.upper(x)
nomes_maiusculos = list(map(f_maiuscula, veiculos))
print(f'nomes maiusculos = {nomes_maiusculos}')