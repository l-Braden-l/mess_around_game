# -- Pygame Game Template -- #

import pygame
import sys
import config # Import the config module 

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


# -- Draw Circle -- #
def draw_circle(screen, center, radius, color, thickness):
    # --- Draw circle on window --- #
    pygame.draw.circle(screen, color, center, radius, thickness)


# -- Draw Rectangle -- #
def draw_rectangle(screen, rect, color, thickness, border_radius):
    # --- Draw rect on window --- #
    pygame.draw.rect(screen, color, rect, thickness, border_radius)


# -- Draw Polygon -- #
def draw_poly(screen, color, points,thickness):
    # --- Draw polygon on window --- #
    pygame.draw.polygon(screen, color, points,thickness)



# -- Main -- #
def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here



   running = True
   while running:
      running = handle_events()

      # -- Handle Key Pressed For Movement -- #

      screen.fill(config.WHITE) # Use color from config

      #-- Click Icon --#
      if pygame.mouse.get_pressed()[0] == False:

         # --- Circle Drawn out line --- #
         circle_center = (370, 295)
         circle_radius = 100
         circle_color = config.BLACK
         circle_thick = 4
         draw_circle(screen, circle_center, circle_radius, circle_color, circle_thick)

         # --- triangle Drawn --- #
         points = [(340, 250), #top left
                     (340, 340), #bottom left
                     (430, 300)  #right
                     ]
         thickness = 0
         draw_poly(screen, config.BLACK, points,thickness)

         # --- triangle Drawn outline --- #
         points = [(340, 250), #top left
                     (340, 340), #bottom left
                     (430, 300)  #right
                     ]
         thickness = 4
         draw_poly(screen, config.WHITE, points,thickness)






      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()