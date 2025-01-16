import pygame
from os.path import join
from random import randint

# general setup 
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
running = True

surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_position = [(randint(0, WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  display_surface.fill('darkgray')
  for pos in star_position:
    display_surface.blit(star_surf, pos)
  player_rect.left += 0.1
  display_surface.blit(player_surf, player_rect)
  pygame.display.update()
pygame.quit()
