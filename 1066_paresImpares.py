a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
num = []
pares = []
impares = []
positivos = []
negativos= []

num.extend([a, b, c, d, e])
for i in num:
    if i > 0:
        positivos.extend([i])
    if i < 0:
        negativos.extend([i])
    if i % 2 == 0:
        pares.extend([i])
    else:
        impares.extend([i])

print (f'{len(pares)} valor(es) par(es)')
print (f'{len(impares)} valor(es) impar(es)')
print (f'{len(positivos)} valor(es) positivo(s)')
print (f'{len(negativos)} valor(es) negativo(s)', end="\n")