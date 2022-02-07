
from pygame import mixer
import pygame

pygame.mixer.init()
pygame.init()

mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play()
pygame.event.wait()
