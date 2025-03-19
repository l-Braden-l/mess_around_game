# -- Pygame Game Template -- #

import pygame
import sys
import config # Import the config module 

# -- Draw Text -- #
def draw_text(screen, text, x, y, font_size, color, font_name=None, bold=False, italic=False):
   if font_name: 
      font = pygame.font.Font(font_name, font_size)
   else:
      font = pygame.font.Font(None, font_size)

   font.set_bold(bold)
   font.set_italic(italic)
   text_surface = font.render(text, True, color)
   screen.blit(text_surface, (x, y))

# -- initilize -- #
def init_game (): 
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

# -- Events -- #
def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True


# -- Main -- #
def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here

   
   # -- Define Shape --#
   shape = "o"
   font_size1 = 48
   color1 = config.WHITE
   x1, y1 = (20000, 25000)

   # -- Define Text -- #
   text2 = "Press anywhere on the screen to continue!"
   font_size2 = 20
   color2 = config.WHITE

   text3 = "Fly Around!"
   font_size3 = 25
   color3 = config.WHITE
   x2, y2 = (20000, 25000)



   running = True
   while running:
      running = handle_events()

      screen.fill(config.BLACK) # Use color from config

      # -- If Press Anywhere -- #
      if pygame.mouse.get_pressed()[0] == True:
         text2 = ""
         x1, y1 = (375, 300)
         x2, y2 = (335, 200)

      # -- Handle Key Pressed For Movement -- #
      keys = pygame.key.get_pressed()
      if keys [pygame.K_UP]:
         y1 -=5 # Move Up
      if keys [pygame.K_DOWN]:
         y1 +=5 # Move Down
      if keys [pygame.K_LEFT]:
         x1 -= 5 # Move Left
      if keys [pygame.K_RIGHT]:
         x1 +=5 # Move Right

      

      # -- Draw Shape On Screen -- # 
      draw_text(screen, shape, x1, y1, font_size1, color1)

      # -- Draw Other Text On Screen -- # 
      draw_text(screen, text2, 240, 300, font_size2, color2)
      draw_text(screen, text3, x2, y2, font_size3, color3)



      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()