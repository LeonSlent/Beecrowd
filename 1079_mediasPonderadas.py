N = int(input())

for _ in range(N):
    a, b, c = map(float, input().split())
    media_ponderada = (a * 2 + b * 3 + c * 5) / 10
    print(f"{media_ponderada:.1f}")
