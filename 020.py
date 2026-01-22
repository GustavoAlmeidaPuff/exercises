# ## 020
#
# ### O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = ['João', 'Maria', 'Pedro', 'Ana'] # lista de alunos

ordem = random.shuffle(alunos) # embaralha a lista de alunos usando a função shuffle da biblioteca random

print(f'A ordem de apresentação é: {ordem}') # exibe a ordem de apresentação usando a função format da biblioteca random