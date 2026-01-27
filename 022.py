# ## 022
#
# ### Crie um programa que leia o nome completo de uma pessoa e mostre:
# * O nome com todas as letras maiúsculas e minúsculas.
# * Quantas letras ao todo (sem considerar espaços).
# * Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))
print("analizando seu nome...")
print("seu nome em maiusculas é:", nome.upper())
print("seu nome em minusculas é:", nome.lower())
print("seu nome tem", len(nome) - nome.count(" "), "letras")
print("seu primeiro nome tem", nome.find(" "), "letras")