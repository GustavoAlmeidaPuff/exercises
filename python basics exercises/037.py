# ## 037
#
# ### Escreva um programa em que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Digite um número inteiro: "))

base = int(input("Digite a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal: "))

if base == 1:
    print(f"O número {numero} em binário é {bin(numero)}")
elif base == 2:
    print(f"O número {numero} em octal é {oct(numero)}")
elif base == 3:
    print(f"O número {numero} em hexadecimal é {hex(numero)}")
else:
    print("Base de conversão inválida")