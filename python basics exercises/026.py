# ## 026
#
# ### Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.


frase = str(input("Digite uma frase: "))
quantidade = 0
primeira_posicao = -1
ultima_posicao = -1

for i in range(len(frase)):
    if frase[i] == "a" or frase[i] == "A":
        quantidade += 1
        ultima_posicao = i
        if quantidade == 1:
            primeira_posicao = i

print("A letra A aparece", quantidade, "vezes na frase.")
if quantidade > 0:
    print("A primeira letra A apareceu na posição", primeira_posicao)
    print("A última letra A apareceu na posição", ultima_posicao)
else:
    print('A frase não possui a letra "A".')