# Programa que calcula a média de três notas fornecidas pelo usuário

# Receber as três notas do usuário
notas = []
for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Digite a {i}ª nota (0-10): "))
            if nota < 0 or nota > 10:
                print("Erro! Digite uma nota entre 0 e 10!")
                continue
            notas.append(nota)
            break
        except ValueError:
            print("Erro! Digite um número válido!")

# Calcular a média
media = sum(notas) / len(notas)

# Classificar o resultado
if media >= 7:
    classificacao = "APROVADO"
elif media >= 5:
    classificacao = "RECUPERAÇÃO"
else:
    classificacao = "REPROVADO"

# Exibir os resultados
print(f"\n{'='*50}")
print(f"CÁLCULO DE MÉDIA")
print(f"{'='*50}")
print(f"Nota 1: {notas[0]}")
print(f"Nota 2: {notas[1]}")
print(f"Nota 3: {notas[2]}")
print(f"-"*50)
print(f"Média: {media:.2f}")
print(f"Classificação: {classificacao}")
print(f"{'='*50}")
