lista1 = []
x, y, z = map(int, input().split())
lista1.extend([x, y, z])

sortedList = lista1.copy()
lista1.sort()

for x in lista1:
    print (x)
print()
for y in sortedList:
    print (y, end="\n")
