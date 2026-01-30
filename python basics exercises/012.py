# ## 012
#
# ### Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Solicita o preço do produto ao usuário
preco = float(input('Digite o preço do produto: '))

# Calcula o desconto de 5%
desconto = preco * 0.05

# Calcula o novo preço com o desconto
novo_preco = preco - desconto

# Exibe o novo preço com 2 casas decimais
print(f'O preço do produto com 5% de desconto é: {novo_preco:.2f}')