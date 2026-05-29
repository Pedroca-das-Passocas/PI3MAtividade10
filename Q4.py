maior = None
menor = None
soma = 0
for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))
    soma += num
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num
media = soma / 5
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Média: {media:.2f}")