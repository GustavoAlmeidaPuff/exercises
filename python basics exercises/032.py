# ## 032
#
# ### Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Digite um ano qualquer: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # É bissexto se for divisível por 4 e não por 100, ou se for divisível por 400.
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")