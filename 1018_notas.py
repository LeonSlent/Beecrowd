valor = int (input())
notas = [100, 50, 20, 10, 5, 2, 1]

print (valor)

for quantidade in notas:
    qtdNotas = valor // quantidade
    valor %= quantidade
    print (f'{qtdNotas} nota(s) de R$ {quantidade},00', end="\n")