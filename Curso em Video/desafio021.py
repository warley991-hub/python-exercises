import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega a música
pygame.mixer.music.load('musica.mp3')

# Dá o play
pygame.mixer.music.play()

# O comando input() trava a tela para o programa não fechar e a música parar na hora
input('Aperte Enter para parar a música...')