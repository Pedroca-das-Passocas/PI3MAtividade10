print("Números divisíveis por 4:")
for i in range(1, 9):
    num = int(input(f"Digite o {i}º número: "))
    if num % 4 == 0:
        print(num)