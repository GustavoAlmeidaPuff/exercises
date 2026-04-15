# ## 027
# Identificador do exercício.
#
# ### Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Enunciado do exercício.

nome = str(input("Digite seu nome completo: "))  # Lê o nome completo digitado pelo usuário.
primeiro_nome = ""  # Variável que vai guardar o primeiro nome no final.
ultimo_nome = ""  # Variável que vai guardar o último nome no final.

partes = []  # Lista que armazenará cada "pedaço" (cada nome) separado manualmente.
parte_atual = ""  # Acumulador para montar uma palavra caractere por caractere.

for caractere in nome.strip():  # Percorre o texto sem espaços extras no começo/fim.
    if caractere != " ":  # Se não for espaço, ainda estamos dentro de uma palavra.
        parte_atual += caractere  # Adiciona o caractere à palavra que está sendo montada.
    elif parte_atual != "":  # Se encontrou espaço e já existe palavra montada...
        partes.append(parte_atual)  # ...salva a palavra na lista de partes.
        parte_atual = ""  # Limpa o acumulador para começar a próxima palavra.

if parte_atual != "":  # Depois do loop, verifica se ainda restou uma palavra não salva.
    partes.append(parte_atual)  # Salva a última palavra (normalmente o último nome).

if partes:  # Garante que há pelo menos uma palavra para evitar erro de índice.
    primeiro_nome = partes[0]  # Primeiro elemento da lista = primeiro nome.
    ultimo_nome = partes[-1]  # Último elemento da lista = último nome.

print("Seu primeiro nome é", primeiro_nome)  # Exibe o primeiro nome encontrado.
print("Seu último nome é", ultimo_nome)  # Exibe o último nome encontrado.