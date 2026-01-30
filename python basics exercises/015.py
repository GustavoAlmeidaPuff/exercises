# ## 015
#
# ### Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorridos = float(input('Digite a quantidade de Km percorridos: '))

# Solicita a quantidade de dias alugados ao usuário
dias_alugados = int(input('Digite a quantidade de dias alugados: '))

# Define os preços por dia e por Km
preco_por_dia = 60
preco_por_km = 0.15

# Calcula o preço total a pagar
preco_total = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)

# Exibe o preço total a pagar com 2 casas decimais
print(f'O preço a pagar é: {preco_total:.2f}')