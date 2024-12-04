# import pygame
#
# import pygame_widgets
# from pygame_widgets.button import ButtonArray
#
# # Set up Pygame
# pygame.init()
# win = pygame.display.set_mode((600, 600))
#
#
# colors = {"base": (255, 0, 0), "hover": (0, 0, 255), "press": (0, 255, 0)}
# # Creates an array of buttons
# buttonArray = ButtonArray(
#     # Mandatory Parameters
#     win,  # Surface to place button array on
#     50,  # X-coordinate
#     50,  # Y-coordinate
#     500,  # Width
#     500,  # Height
#     (1, 4),  # Shape: 2 buttons wide, 2 buttons tall
#     #border=100,  # Distance between buttons and edge of array
#     texts=('1', '2', '3', '4', '5', '6'),  # Sets the texts of each button (counts left to right then top to bottom)
#     # colour=colors["base"],
#     inactiveColours=[colors["base"]]*6,  # Colour of button when not being interacted with
#     hoverColours=[colors["hover"]]*6,  # Colour of button when being hovered over
#     pressedColours=[colors["press"]]*6,  # Colour of button when being clicked
#     onClicks=(lambda: print('1'), lambda: print('2'), lambda: print('3'), lambda: print('4'), lambda: print('5'), lambda: print('6'))
# )
#
# run = True
# while run:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             run = False
#             quit()
#
#     pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
#     pygame.display.update()



# def button(self, coords, layout, colors, font, func):
#     self.base_buttons = ButtonArray(
#         # Mandatory Parameters
#         self.parent.display,  # Surface to place button array on
#         coords[0],  # X-coordinate of top left corner
#         coords[1],  # Y-coordinate of top left corner
#         coords[2] - coords[0],
#         coords[3] - coords[1],  # Height
#         layout,  # Shape: 2 buttons wide, 2 buttons tall
#         # border=100,  # Distance between buttons and edge of array
#         texts=('1', '2', '3', '4'),  # Sets the texts of each button (counts left to right then top to bottom)
#         inactiveColour=colors["base"],  # Colour of button when not being interacted with
#         hoverColour=colors["hover"],  # Colour of button when being hovered over
#         pressedColour=colors["press"],  # Colour of button when being clicked
#         # When clicked, print number
#         onClicks=(lambda: print('1'), lambda: print('2'), lambda: print('3'), lambda: print('4'))
#     )
#
#
#     self.button = Button(
#         # Mandatory Parameters
#         self.parent.display,  # Surface to place button on
#         coords[0],  # X-coordinate of top left corner
#         coords[1],  # Y-coordinate of top left corner
#         coords[2]-coords[0],
#         coords[3]-coords[1],
#         text=font["text"],  # Text to display
#         fontSize=font["size"],  # Size of font
#         #margin=20,  # Minimum distance between text/image and edge of button
#         inactiveColour=colors["base"],  # Colour of button when not being interacted with
#         hoverColour=colors["hover"],  # Colour of button when being hovered over
#         pressedColour=colors["press"],  # Colour of button when being clicked
#         onClick=func  # Function to call when clicked on
#     )

# label text
import pygame as pg
import sys

pg.init()

sc = pg.display.set_mode((400, 300))
sc.fill((200, 255, 200))

font = pg.font.Font(None, 72)
text = font.render("Hello Wold", True, (0, 100, 0))
place = text.get_rect(center=(200, 150))
sc.blit(text, place)

pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT]:
        place.x -= 1
    elif pressed[pg.K_RIGHT]:
        place.x += 1

    sc.fill((200, 255, 200))
    sc.blit(text, place)

    pg.display.update()

    pg.time.delay(20)