# ## 018
#
# ### Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math # importa a biblioteca math para calcular o seno, cosseno e tangente

angulo = float(input('Digite o ângulo: ')) # solicita o ângulo ao usuário

seno = math.sin(math.radians(angulo)) # calcula o seno do ângulo usando a função sin da biblioteca math e convertendo o ângulo para radianos
cosseno = math.cos(math.radians(angulo)) # calcula o cosseno do ângulo usando a função cos da biblioteca math e convertendo o ângulo para radianos
tangente = math.tan(math.radians(angulo)) # calcula a tangente do ângulo usando a função tan da biblioteca math e convertendo o ângulo para radianos

print(f'O seno de {angulo} é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}') # exibe o seno, cosseno e tangente do ângulo com 2 casas decimais usando a função format da biblioteca math