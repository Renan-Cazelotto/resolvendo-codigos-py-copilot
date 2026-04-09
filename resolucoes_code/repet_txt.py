# Programa que recebe uma string e um número inteiro, e retorna a string repetida

# Receber a string do usuário
texto = input("Digite uma string: ")

# Receber o número inteiro do usuário
while True:
    try:
        numero = int(input("Digite o número de repetições (inteiro positivo): "))
        if numero < 0:
            print("Por favor, digite um número positivo!")
            continue
        break
    except ValueError:
        print("Erro! Digite um número inteiro válido!")

# Repetir a string pelo número de vezes informado
resultado = texto * numero

# Exibir o resultado
print(f"\nString original: {texto}")
print(f"Número de repetições: {numero}")
print(f"Resultado: {resultado}")