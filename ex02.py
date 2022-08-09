# 2 -programa para contar a quantidade de números
# pares entre dois números quaisquer?

# entrada de dados
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# tratamento de erro
if num1 > num2:
    print("O primeiro número deve ser menor que o segundo")
elif num1 == num2:
    print("Os números devem ser diferentes")
else:
    # contador de numeros pares
    quantidadePar = 0
    numero1 = num1
    numero2 = num2
    while numero1 <= numero2:
        if numero1 % 2 == 0:
            quantidadePar += 1
        numero1 += 1
    print(f"A quantidade de numeros pares entre {num1} e {num2} é {quantidadePar}")