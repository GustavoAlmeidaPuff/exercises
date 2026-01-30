# 004
#
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# *tipo primitivo
# *só tem espaços?
# *é um numero?
# *é alfabético?
# *é alfanumérico?
# *esta em maiúsculas?
# *esta em minusculas?
# *esta capitalizada?
#

var = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(var))
print('Só tem espaços?', var.isspace())
print('É um numero?', var.isnumeric())
print('É alfabético?', var.isalpha())
print('É alfanumérico?', var.isalnum())
print('Está em maiúsculas?', var.isupper())
print('Está em minúsculas?', var.islower())
print('Está capitalizada?', var.istitle())

input('Pressione Enter para sair...')