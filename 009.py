# 009
#
# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
#

numero = int(input("digite um numero pra saber a tuabuada: "))

# com as piores praticas

# vezes1 = (numero) * 1
# vezes2 = (numero) * 2
# vezes3 = (numero) * 3
# vezes4 = (numero) * 4
# vezes5 = (numero) * 5
# vezes6 = (numero) * 6
# vezes7 = (numero) * 7
# vezes8 = (numero) * 8
# vezes9 = (numero) * 9
# vezes10 = (numero) * 10
# print(f"A tabuada de {numero} é: \n\n{numero} * 1 = {vezes1}\n{numero} * 2 = {vezes2}\n{numero} * 3 = {vezes3}\n{numero} * 4 = {vezes4}\n{numero} * 5 = {vezes5}\n{numero} * 6 = {vezes6}\n{numero} * 7 = {vezes7}\n{numero} * 8 = {vezes8}\n{numero} * 9 = {vezes9}\n{numero} * 10 = {vezes10}")


# ou...(com for, melhor pratica)

for i in range(1, 11):
    print(f"{numero} * {i} = {numero * i}")