soma = 0
for i in range(1, 21):
    valor = float(input(f"Digite o {i}º valor: "))
    soma += valor
media = soma / 20
print(f"Média: {media:.2f}")