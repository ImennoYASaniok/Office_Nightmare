import pygame
import pygame_widgets
from pygame_widgets.button import ButtonArray

from menu import Menu
from game import Game

class Main():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.display_w, self.display_h = pygame.display.Info().current_w-10,pygame.display.Info().current_h-50
        self.fps = 30
        self.running = 1
        self.type_display = "menu"
        self.flag_type_display = 0 # 0 - menu | 1 - game
        self.colors = {
            "light": (187, 148, 87),
            "base1": (153, 88, 42),
            "base2": (111, 29, 27),
            "dark": (67, 40, 24)
        }

        self.display = pygame.display.set_mode((self.display_w, self.display_h))
        self.display.fill(self.colors["dark"])

        self.menu = Menu(self, self.colors)
        self.game = Game(self, self.colors)

        pygame.display.set_caption("Office Nightmare")
        self.clock = pygame.time.Clock()


    def buttons(self, coords, layout, texts, fonts, funcs):
        # !!! Если понадобиться разные цвета кнопок - делаем именованный аргумент colors
        return ButtonArray(
            self.display,  # Surface to place button array on
            coords[0], coords[1], coords[2] - coords[0], coords[3] - coords[1],
            layout,
            # border=100,  # Distance between buttons and edge of array
            texts=texts,
            fonts=fonts,
            colour=self.colors["base2"],
            inactiveColours=[self.colors["base1"]]*len(texts),  # Colour of button when not being interacted with
            hoverColours=[self.colors["base2"]]*len(texts),  # Colour of button when being hovered over
            pressedColours=[self.colors["light"]]*len(texts),  # Colour of button when being clicked
            textColours=[self.colors["light"]]*len(texts),
            onClicks=funcs
        )

    def button(self, coords, layout, text, font, func):
        return ButtonArray(
            self.display,  # Surface to place button array on
            coords[0], coords[1], coords[2] - coords[0], coords[3] - coords[1],
            layout,
            # border=100,  # Distance between buttons and edge of array
            texts=text,
            fonts=font,
            colour=self.colors["base2"],
            inactiveColour=self.colors["base1"],  # Colour of button when not being interacted with
            hoverColour=self.colors["base2"],  # Colour of button when being hovered over
            pressedColours=self.colors["light"],  # Colour of button when being clicked
            textColours=self.colors["light"],
            onClicks=func
        )

    def label_text(self, coords, text, font):
        f = font
        res_label = f.render(text, True, self.colors["light"])
        self.display.blit(res_label, coords)
        pygame.display.update()
        return res_label

    def game_quit(self):
        self.running = 0

    def game_start(self):
        self.type_display = "game"

    def show(self):
        while self.running:
            events = pygame.event.get()
            self.clock.tick(self.fps)

            if self.type_display == "menu" and self.flag_type_display == 0:
                print(self.type_display, self.flag_type_display)
                self.display.fill(self.colors["dark"])
                self.menu.reinstall("show")
                self.game.reinstall("hide")
                self.flag_type_display = 1
            elif self.type_display == "game" and self.flag_type_display == 1:
                print(self.type_display, self.flag_type_display)
                self.display.fill(self.colors["dark"])
                self.menu.reinstall("hide")
                self.game.reinstall("show")
                self.flag_type_display = 0


            for event in events:
                if event.type == pygame.QUIT: self.running = False
            pygame_widgets.update(events)
            pygame.display.update()

if __name__ == "__main__":
    menu = Main()
    menu.show()