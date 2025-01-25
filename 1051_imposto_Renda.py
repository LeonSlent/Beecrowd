salario = float(input())

if salario <= 2000:
    print("Isento")
elif salario <= 3000:
    imposto = (salario - 2000) * 0.08
    print(f"R$ {imposto:.2f}")
elif salario <= 4500:
    imposto = (salario - 3000) * 0.18 + 80
    print(f"R$ {imposto:.2f}")
else:
    imposto = (salario - 4500) * 0.28 + 350
    print(f"R$ {imposto:.2f}")
