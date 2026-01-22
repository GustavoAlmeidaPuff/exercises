# ## 019
#
# ### Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

alunos = ['João', 'Maria', 'Pedro', 'Ana'] # lista de alunos

escolhido = random.choice(alunos) # escolhe um aluno aleatório usando a função choice da biblioteca random

print(f'O aluno escolhido foi: {escolhido}') # exibe o aluno escolhido usando a função format da biblioteca random