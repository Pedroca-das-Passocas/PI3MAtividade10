vendas = []
total = 0
for mes in range(1, 7):
    valor = float(input(f"Vendas do mês {mes}: "))
    vendas.append(valor)
    total += valor
media = total / 6
acima_media = 0
for v in vendas:
    if v > media:
        acima_media += 1
print(f"Total de vendas: R${total:.2f}")
print(f"Média mensal: R${media:.2f}")
print(f"Meses com vendas acima da média: {acima_media}")