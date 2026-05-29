n = input("Digite um número: ")
d = input("Digite um dígito (0 a 9): ")
contagem = 0
for digito in n:
    if digito == d:
        contagem += 1
print(f"O dígito {d} aparece {contagem} vezes")