import pygame

width = 1800
height = 960

pygame.init()
screen = pygame.display.set_mode((width,height))
running = True
pygame.mixer.init()
pygame.mixer.music.load('/Users/jorahzo/Desktop/code/git/tarteria.system/idunno.mp3')
pygame.mixer.music.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



