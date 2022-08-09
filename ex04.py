
# 4 - Programa que calcule o fatorial de um número.

# 5! = 5 * 4 * 3 * 2 * 1

# entrada de dados
num = int(input("Digite o número: "))
numero1 = num

# processamento de dados
fatorial = 1
while num > 1:
    fatorial *= num # fatorial = fatorial * num
    num -= 1  # num = num - 1
print(f"O fatorial de {numero1} é {fatorial}")
print("fim do programa")

