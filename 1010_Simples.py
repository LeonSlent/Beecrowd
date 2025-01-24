valores1 = input().split()
valores2 = input().split()

a = int(valores1[0])
b = int(valores1[1])
c = float(valores1[2])

x = int(valores2[0])
y = int(valores2[1])
z = float(valores2[2])

valor1 = b * c
valor2 = y * z
total = valor1 + valor2
print (f'VALOR A PAGAR: R$ {total:.2f}', end="\n")

