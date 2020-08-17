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
  snek_pos = [pygame.math.Vector2(0,0)]

  # Constructor, called when class is instantiated
  def __init__(self):
    pygame.display.set_icon(self.snek_body)
    pygame.display.set_caption("Snek Game")
    self._fps = 5
    self._clock = pygame.time.Clock()
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
        self.arrows[1] = False
        self.arrows[2] = False
        self.arrows[3] = False
      elif event.key == pygame.K_RIGHT:
        self.arrows[1] = True
        self.arrows[0] = False
        self.arrows[2] = False
        self.arrows[3] = False
      elif event.key == pygame.K_DOWN:
        self.arrows[2] = True
        self.arrows[0] = False
        self.arrows[1] = False
        self.arrows[3] = False
      elif event.key == pygame.K_LEFT:
        self.arrows[3] = True
        self.arrows[0] = False
        self.arrows[1] = False
        self.arrows[2] = False

    # if event.type == pygame.KEYUP:
    #   if event.key == pygame.K_UP:
    #     self.arrows[0] = False
    #   elif event.key == pygame.K_RIGHT:
    #     self.arrows[1] = False
    #   elif event.key == pygame.K_DOWN:
    #     self.arrows[2] = False
    #   elif event.key == pygame.K_LEFT:
    #     self.arrows[3] = False
    

  def first_update(self):
    self.snek_pos[0] = pygame.math.Vector2(10,10)

    # Put the food somewhere at random
    self.regenerate_food()

  # Game loop, handles logic
  def on_update(self):
    # Update direction
    if self.arrows[0] == True and (self.cur_direction != 2):
      self.cur_direction = 0
    elif self.arrows[1] == True and (self.cur_direction != 3):
      self.cur_direction = 1
    elif self.arrows[2] == True and (self.cur_direction != 0):
      self.cur_direction = 2
    elif self.arrows[3] == True and (self.cur_direction != 1):
      self.cur_direction = 3

    # Update position of various body parts
    if self.cur_direction >= 0 :
      for x in range(len(self.snek_pos), 0, -1):
        if(x > 1):
          self.snek_pos[x - 1].x = self.snek_pos[x - 2].x
          self.snek_pos[x - 1].y = self.snek_pos[x - 2].y

    if self.cur_direction == 0 :
      self.snek_pos[0] += pygame.math.Vector2(0,-1)
    elif self.cur_direction == 1 :
      self.snek_pos[0] += pygame.math.Vector2(1,0)
    elif self.cur_direction == 2 :
      self.snek_pos[0] += pygame.math.Vector2(0,1)
    elif self.cur_direction == 3 :
      self.snek_pos[0] += pygame.math.Vector2(-1,0)
    
    self.check_for_collisions()

    if self.snek_pos[0] == self.food_pos:
      self.regenerate_food()
      self.make_snek_bigger()


  def first_draw(self):
    self._screen.blit(self.game_bg, (0,0))

    starting_food_px = (self.food_pos * self.snek_body_width)
    print("Starting food pos = " + str(self.food_pos) + " and resulting px = " + str(starting_food_px))
    self._screen.blit(self.snek_food, starting_food_px )

    starting_snek_px = (self.snek_pos[0] * self.snek_body_width)
    print("Starting Snek pos = " + str(self.food_pos) + " and resulting px = " + str(starting_snek_px))
    self._screen.blit(self.snek_body, starting_snek_px)
    
    pygame.display.update()

  # Called after on_loop , renders state to the screen
  def on_draw(self):
    self._screen.fill( (0,0,0) )
    self._screen.blit(self.game_bg, (0,0))
    pygame.display.update()
    
    self._screen.blit(self.snek_food, self.food_pos * self.snek_body_width)

    for pos in self.snek_pos :
      cur_px = pos * self.snek_body_width
      self._screen.blit(self.snek_body, cur_px)

    pygame.display.update()
    self._clock.tick(self._fps)

  def make_snek_bigger(self):
    snek_len = len(self.snek_pos)
    self.snek_pos.append(pygame.math.Vector2(
      self.snek_pos[snek_len - 1][0],
      self.snek_pos[snek_len - 1][1]
    ))
    self._fps += 1

  def regenerate_food(self):
    self.food_pos = pygame.math.Vector2(random.randint(1,19), random.randint(1,19))
    while self.food_pos.x == self.snek_pos[0].x and self.food_pos.y == self.snek_pos[0].y :
      self.food_pos = pygame.math.Vector2(random.randint(1,19), random.randint(1,19))

  def check_for_collisions(self):
    if(self.snek_pos[0].x == 0 or self.snek_pos[0].x == 20 or self.snek_pos[0].y == 0 or self.snek_pos[0].y == 20):
      self.game_over()

    for x in range(len(self.snek_pos), 0, -1):
      if x > 2 :
        if self.snek_pos[0].x == self.snek_pos[x - 1].x and self.snek_pos[0].y == self.snek_pos[x - 1].y:
          self.game_over()

  def game_over(self):
    print("game over")
    self._running = False

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
