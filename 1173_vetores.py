n = [0] *10
n[0]= int (input())
for i in range (1, 10):
    n[i] = n[i-1] * 2

for i in range(10):
    print(f"N[{i}] = {n[i]}")