# ## 036
#
# ### Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário do comprador: "))
anos = int(input("Digite em quantos anos o comprador vai pagar: "))

valor_prestacao = valor_casa / (anos * 12)

if valor_prestacao > salario * 0.30:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo APROVADO!")

print(f"A prestação mensal é de R${valor_prestacao:.2f}, isso é {valor_prestacao / salario * 100}% do salário do comprador.")