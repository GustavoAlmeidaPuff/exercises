# ## 039
#
# ### Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = 2026 - ano_nascimento

if idade < 18:
    print("Você ainda vai se alistar ao serviço militar")
elif idade == 18:
    print("É a hora exata de se alistar")
else:
    print("Você já passou do tempo do alistamento")
