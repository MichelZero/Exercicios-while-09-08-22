# 1 - Programa que imprime a quantidade de números
# pares de 100 até 200, incluindo-os.

# a) como encontra os numeros pares de 100 até 200?
# numero1 = 100
# if numero1 % 2 == 0:
#     print(f"{numero1} é par")
# B) quantidade de numeros pares de 100 até 200?
# quantidadePar = 0
# numero1 = 100
# if numero1 % 2 == 0:
#     print(f"{numero1} é par")
#     quantidadePar += 1 # quantidadePar = quantidadePar + 1

# c) quantidade de numeros pares de 100 até 200?
quantidadePar = 0
numero1 = 100
numero2 = 200

while numero1 <= numero2:
    if numero1 % 2 == 0:
        #print(f"{numero1} é par")
        quantidadePar += 1
    numero1 += 1
else:
    print(f"A quantidade de numeros pares de 100 até 200 é {quantidadePar}")

