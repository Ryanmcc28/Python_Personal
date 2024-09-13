import pygame as pyg
from pygame.math import Vector2
import sys
import random

pyg.init()

class SNAKE:

   def __init__(self):
      self.body = [Vector2(5,10),Vector2(5,11),Vector2(5,12)]
      self.direction = Vector2(1,0)
      self.new_block = False

   def draw_snake(self):
     for item in self.body:
        snake_rect = pyg.Rect(int(item.x * cell_size),int(item.y * cell_size),cell_size,cell_size)
        pyg.draw.rect(screen, pyg.Color("forest green"), snake_rect)

   def move_snake(self):
      if  self.new_block == True:
         body_copy = self.body[:]
         body_copy.insert(0,body_copy[0] + self.direction)
         self.body = body_copy[:]
         self.new_block = False
      else:  
         body_copy = self.body[:-1]
         body_copy.insert(0,body_copy[0] + self.direction)
         self.body = body_copy[:]

   def add_block(self):
      self.new_block = True
     
      
         


class FRUIT:
   def __init__(self):
      self.randomize()

   def draw_fruit(self):
      fruit_rect = pyg.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
      pyg.draw.rect(screen,pyg.Color("Red"), fruit_rect)

   def randomize(self):
      self.x = random.randint(0,cell_num - 1)
      self.y = random.randint(0,cell_num - 1)
      self.pos = Vector2(self.x,self.y)
      



class MAIN:
   
   def __init__(self):
      self.snake = SNAKE()
      self.fruit = FRUIT()

   def  update(self):
      self.snake.move_snake()  
      self.check_collision()

   def draw_elements(self):
       self.fruit.draw_fruit()
       self.snake.draw_snake()

   def check_collision(self):
      if  self.fruit.pos == self.snake.body[0]:
         self.fruit.randomize()
         self.snake.add_block()
   
   def check_fail(self):
      if  self.snake.body[0].x < 0 or self.snake.body[0].x >= (cell_num) or self.snake.body[0].y < 0 or self.snake.body[0].y >= (cell_num):
          pyg.quit()
          sys.exit()  

      for index in range(len(self.snake.body) - 1):
        if self.snake.body[0].x == self.snake.body[index + 1].x and self.snake.body[0].y == self.snake.body[index + 1].y:
         pyg.quit()
         sys.exit()
                 

  
        


      
      

cell_size = 40
cell_num = 20
screen = pyg.display.set_mode((cell_num*cell_size,cell_num*cell_size))

clock = pyg.time.Clock()

main_game = MAIN()

SCREEN_UPDATE = pyg.USEREVENT
pyg.time.set_timer(SCREEN_UPDATE,130)

previous_input = ""

counter = 0

#EVENT/GAME LOOP
while True:

  main_game.check_fail()

  for item in pyg.event.get():
      if  item.type == pyg.QUIT:
          pyg.quit()
          sys.exit()    
      if item.type == SCREEN_UPDATE:
         main_game.update()

      if item.type == pyg.KEYDOWN:
         if item.key == pyg.K_w and previous_input != "s":
            previous_input = "w"
            main_game.snake.direction = Vector2(0,-1)            
         elif item.key == pyg.K_s and previous_input != "w":
            previous_input = "s"
            main_game.snake.direction = Vector2(0,1)           
         elif item.key == pyg.K_d and previous_input != "a":
            previous_input = "d"
            main_game.snake.direction = Vector2(1,0)             
         elif item.key == pyg.K_a and previous_input != "d":
            previous_input = "a"
            main_game.snake.direction = Vector2(-1,0)
            

  screen.fill((255,215,235))
  main_game.draw_elements()
  pyg.display.update()
  clock.tick(60)

