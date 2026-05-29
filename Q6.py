produto_maior = 1
maior_consumo = 0
total = 0
for i in range(1, 8):
    consumo = float(input(f"Consumo do produto {i} (kg): "))
    total += consumo
    if consumo > maior_consumo:
        maior_consumo = consumo
        produto_maior = i
print(f"Consumo total: {total} kg")
print(f"Produto que mais consumiu: {produto_maior} com {maior_consumo} kg")