import pygame as pyg
import sys

pyg.init()
screen = pyg.display.set_mode((400,500))

loop = True

clock = pyg.time.Clock()

test_surface = pyg.Surface((100,200))
test_surface.fill((30,75,100))

x_pos = 200
y_pos = 250

test_rectangle = test_surface.get_rect(center = (200,250))

while loop:
  
  for item in pyg.event.get():
      if  item.type == pyg.QUIT:
          pyg.quit()
          sys.exit()
  screen.fill((255,215,235))
  screen.blit(test_surface,test_rectangle)
  pyg.display.update()
  clock.tick(60)
