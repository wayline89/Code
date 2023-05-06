import pygame
pygame.init()
pygame.font.init()

WIDTH = HEIGHT = 600

FPS = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ttt_font = pygame.font.SysFont('Comic Sans MS', 20)

def load_image_scaled(path, size):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, size)
