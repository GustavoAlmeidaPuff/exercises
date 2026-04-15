# ## 028
#
# ### Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou errou, se errou, fale se o numero ta ,ais pra cima ou mais pra baixo. e faça isso virar um loop 
import random

numero = random.randint(0, 1000)

def pedir_numero():
    return int(input("Digite um número entre 0 e 1000: "))

numero_usuario = pedir_numero()

while numero_usuario != numero:
    if numero_usuario > numero:
        print("Você errou! o numero é mais baixo...")
    elif numero_usuario < numero:
        print("Você errou! o numero é mais alto...")
    numero_usuario = pedir_numero()

if numero_usuario == numero:
    print("Você acertou!")
