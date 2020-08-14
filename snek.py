import pygame
from pygame.locals import *

class SnekGame:
  # Assets
  snek_body = pygame.image.load("assets/snakeBody.png")
  snek_food = pygame.image.load("assets/food.png")
  snek_food.set_colorkey((255,255,255)) # Here we tell the game that the color to make transparent is white
  game_bg = pygame.image.load("assets/background.png")

  # Attributes
  snek_pos = (50,50)
  food_pos = (100,100)

  # Constructor, called when class is instantiated
  def __init__(self):
    pygame.display.set_icon(self.snek_body)
    pygame.display.set_caption("Snek Game")

    self._running = True
    self.size = self.weight, self.height = 422, 422
    self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    self._running = True

    self.game_loop()

  # Handles Events
  def on_event(self, event):
    if event.type == pygame.QUIT:
        self._running = False

  # Game loop, handles logic
  def on_update(self):
    pass

  # Called after on_loop , renders state to the screen
  def on_draw(self):

    self._screen.blit(self.game_bg, (0,0))
    self._screen.blit(self.snek_food, self.food_pos)
    self._screen.blit(self.snek_body, self.snek_pos)
    
    pygame.display.flip()
    pass

  # Called when game is closed
  def on_cleanup(self):
    pygame.quit()

  # Calls the other methods
  def game_loop(self):
    while( self._running ):
      for event in pygame.event.get():
        self.on_event(event)
      self.on_update()
      self.on_draw()
    self.on_cleanup()

if __name__ == "__main__" :
  sg = SnekGame()
