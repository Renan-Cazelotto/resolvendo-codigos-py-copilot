# Programa que recebe um número inteiro e verifica se é par ou ímpar

# Receber um número inteiro do usuário
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Erro! Digite um número inteiro válido!")

# Verificar se é par ou ímpar
if numero % 2 == 0:
    resultado = "PAR"
else:
    resultado = "ÍMPAR"

# Exibir o resultado
print(f"\n{'='*40}")
print(f"Número: {numero}")
print(f"Classificação: {resultado}")
print(f"{'='*40}")

# Detalhes adicionais
if numero % 2 == 0:
    print(f"✓ {numero} é divisível por 2 (resto = 0)")
else:
    print(f"✓ {numero} deixa resto 1 quando dividido por 2")
