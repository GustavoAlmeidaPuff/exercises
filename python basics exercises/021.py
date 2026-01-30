# ## 021
# Cabeçalho do exercício 021
#
# ### Faça um programa em que abra e reproduza o áudio de um arquivo MP3.
# Descrição do exercício: criar um programa que abre e reproduz áudio de um arquivo MP3

import pygame  # Importa a biblioteca pygame para reprodução de áudio
import tkinter as tk  # Importa o módulo tkinter com alias 'tk' para interface gráfica
from tkinter import filedialog  # Importa o módulo filedialog do tkinter para diálogo de seleção de arquivo

pygame.init()  # Inicializa todos os módulos do pygame (mixer, display, etc.)

# Abre uma janela para o usuário escolher o arquivo MP3
root = tk.Tk()  # Cria a janela principal do tkinter (necessária para o filedialog funcionar)
root.withdraw()  # Esconde a janela principal do tkinter (para não aparecer na tela)

arquivo = filedialog.askopenfilename(  # Abre o diálogo de seleção de arquivo e armazena o caminho escolhido
    title="Escolha um arquivo MP3",  # Define o título da janela de seleção
    filetypes=[("Arquivos MP3", "*.mp3"), ("Todos os arquivos", "*.*")]  # Define os tipos de arquivo que podem ser selecionados
)

if arquivo:  # Verifica se o usuário selecionou um arquivo (não cancelou o diálogo)
    print(f"Reproduzindo: {arquivo}")  # Exibe uma mensagem informando qual arquivo está sendo reproduzido
    pygame.mixer.music.load(arquivo)  # Carrega o arquivo de áudio no mixer do pygame
    pygame.mixer.music.play()  # Inicia a reprodução do áudio carregado
    
    # Mantém o programa rodando enquanto o áudio toca
    while pygame.mixer.music.get_busy():  # Loop que continua enquanto o áudio estiver sendo reproduzido
        pygame.time.Clock().tick(10)  # Controla a taxa de atualização do loop (10 frames por segundo)
    
    print("Reprodução concluída!")  # Exibe mensagem quando a reprodução terminar
else:  # Caso o usuário tenha cancelado a seleção de arquivo
    print("Nenhum arquivo selecionado.")  # Exibe mensagem informando que nenhum arquivo foi selecionado

pygame.quit()  # Finaliza todos os módulos do pygame e libera os recursos


