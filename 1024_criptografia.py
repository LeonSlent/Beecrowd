def criptografar(mensagem):
    mensagem = ''.join(
        chr(ord(c) + 3) if c.isalpha() else c
        for c in mensagem
    )
    mensagem = mensagem[::-1]
    meio = len(mensagem) // 2
    mensagem = ''.join(
        chr(ord(c) - 1) if i >= meio else c
        for i, c in enumerate(mensagem)
    )
    return mensagem

n = int(input())
for _ in range(n):
    linha = input().strip()
    print(criptografar(linha))