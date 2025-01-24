valor = float(input())
total = int(valor)
centavos = int(round((valor - total) * 100))
cedulas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]

print ('NOTAS:')

for cedulaAtual in cedulas:
    nCedulas = total // cedulaAtual
    total %= cedulaAtual
    print (f'{nCedulas} nota(s) de R$ {cedulaAtual:.2f}')

print ('MOEDAS:')

centavos += total * 100

for moedaAtual in moedas:
    nMoedas = centavos // moedaAtual
    centavos %= moedaAtual
    print (f'{nMoedas} moeda(s) de R$ {moedaAtual / 100:.2f}', end="\n")