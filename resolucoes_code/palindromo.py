# Programa que verifica se uma palavra é um palíndromo

# Receber a palavra do usuário
palavra = input("Digite uma palavra: ").strip().lower()

# Remover espaços em branco e caracteres especiais
palavra_limpa = ''.join(c for c in palavra if c.isalnum())

# Verificar se é palíndromo
palavra_invertida = palavra_limpa[::-1]
eh_palindromo = palavra_limpa == palavra_invertida

# Exibir os resultados
print(f"\n{'='*50}")
print(f"VERIFICAÇÃO DE PALÍNDROMO")
print(f"{'='*50}")
print(f"Palavra original: {palavra}")
print(f"Palavra limpa: {palavra_limpa}")
print(f"Palavra invertida: {palavra_invertida}")
print(f"-"*50)

if eh_palindromo:
    print(f"✓ '{palavra}' É UM PALÍNDROMO!")
else:
    print(f"✗ '{palavra}' NÃO é um palíndromo.")

print(f"{'='*50}")

# Exemplos de palíndromos
print("\nExemplos de palíndromos:")
print("  • ama")
print("  • radar")
print("  • arara")
print("  • salas")
print("  • anilina")
