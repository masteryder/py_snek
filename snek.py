import pygame
import random
from pygame.locals import *

class SnekGame:
  
  # Assets
  snek_body = pygame.image.load("assets/snakeBody.png")
  snek_food = pygame.image.load("assets/food.png")
  snek_food.set_colorkey((255,255,255)) # Here we tell the game that the color to make transparent is white
  game_bg = pygame.image.load("assets/background.png")
  wall_thickness = 10 #px
  snek_body_width = 20 #px

  # Game Attributes
  snake_length = 1
  points = 0
  arrows = [False, False, False, False] # Up, Right, Down, Left
  cur_direction = -1 # -1 = no direction
  snek_pos = pygame.math.Vector2(0,0)

  # Constructor, called when class is instantiated
  def __init__(self):
    pygame.display.set_icon(self.snek_body)
    pygame.display.set_caption("Snek Game")

    self._running = True
    self.size = self.weight, self.height = 420, 420
    self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

  # Handles Events
  def on_event(self, event):
    if event.type == pygame.QUIT:
      self._running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        self.arrows[0] = True
      elif event.key == pygame.K_RIGHT:
        self.arrows[1] = True
      elif event.key == pygame.K_DOWN:
        self.arrows[2] = True
      elif event.key == pygame.K_LEFT:
        self.arrows[3] = True
      print(self.arrows)

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        self.arrows[0] = False
      elif event.key == pygame.K_RIGHT:
        self.arrows[1] = False
      elif event.key == pygame.K_DOWN:
        self.arrows[2] = False
      elif event.key == pygame.K_LEFT:
        self.arrows[3] = False
    

  def first_update(self):
    self.snek_pos = pygame.math.Vector2(10,10)

    # Put the food somewhere at random
    self.food_pos = pygame.math.Vector2(random.randint(0,20), random.randint(0,20))
    while self.food_pos.x == 10 and self.food_pos.y == 10 :
      self.food_pos = pygame.math.Vector2(random.randint(0,20), random.randint(0,20))

  # Game loop, handles logic
  def on_update(self):

    if self.arrows[0] == True and (self.cur_direction != 2):
      self.cur_direction = 0
    elif self.arrows[1] == True and (self.cur_direction != 3):
      self.cur_direction = 1
    elif self.arrows[2] == True and (self.cur_direction != 0):
      self.cur_direction = 2
    elif self.arrows[3] == True and (self.cur_direction != 1):
      self.cur_direction = 3
    
    if self.cur_direction >= 0 :
      if self.cur_direction == 0 :
        self.snek_pos = self.snek_pos + pygame.math.Vector2(0,-1)
      elif self.cur_direction == 1 :
        self.snek_pos = self.snek_pos + pygame.math.Vector2(1,0)
      elif self.cur_direction == 2 :
        self.snek_pos = self.snek_pos + pygame.math.Vector2(0,1)
      elif self.cur_direction == 3 :
        self.snek_pos = self.snek_pos + pygame.math.Vector2(-1,0)


  def first_draw(self):
    self._screen.blit(self.game_bg, (0,0))

    starting_food_px = (self.food_pos * self.snek_body_width)
    print("Starting food pos = " + str(self.food_pos) + " and resulting px = " + str(starting_food_px))
    self._screen.blit(self.snek_food, starting_food_px )

    starting_snek_px = (self.snek_pos * self.snek_body_width)
    print("Starting Snek pos = " + str(self.food_pos) + " and resulting px = " + str(starting_snek_px))
    self._screen.blit(self.snek_body, starting_snek_px)
    
    pygame.display.flip()

  # Called after on_loop , renders state to the screen
  def on_draw(self):
    snek_px = (self.snek_pos * self.snek_body_width)
    self._screen.blit(self.snek_body, snek_px)
    pygame.display.flip()


  # Called when game is closed
  def on_cleanup(self):
    pygame.quit()

  # Calls the other methods
  def game_loop(self):
    self._running = True
    self.first_update()
    self.first_draw()
    while( self._running ):
      for event in pygame.event.get():
        self.on_event(event)
      self.on_update()
      self.on_draw()
    self.on_cleanup()

if __name__ == "__main__" :
  sg = SnekGame()
  sg.game_loop()
