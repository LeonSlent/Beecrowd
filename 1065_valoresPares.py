a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
lista = []
par = []
lista.extend([a, b, c, d, e])
for i in lista:
    if i % 2 == 0:
        par.append(i)

print(len(par), 'valores pares', end="\n")
