# Programa que solicita dois números e realiza operações matemáticas simples

# Receber os dois números do usuário
while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Erro! Digite números válidos!")

# Calcular operações simples
soma = numero1 + numero2
diferenca = numero1 - numero2
produto = numero1 * numero2

# Divisão com tratamento de erro
if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "indefinida (divisão por zero)"

# Exibir os resultados
print(f"\n{'='*40}")
print(f"Número 1: {numero1}")
print(f"Número 2: {numero2}")
print(f"{'='*40}")
print(f"Soma: {numero1} + {numero2} = {soma}")
print(f"Subtração: {numero1} - {numero2} = {diferenca}")
print(f"Multiplicação: {numero1} × {numero2} = {produto}")
print(f"Divisão: {numero1} ÷ {numero2} = {divisao}")
print(f"{'='*40}")