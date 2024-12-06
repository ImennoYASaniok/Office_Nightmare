import pygame
import pygame_widgets
from pygame_widgets.button import ButtonArray

from menu import Menu

class Main():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.display_w, self.display_h = pygame.display.Info().current_w-10,pygame.display.Info().current_h-50
        self.fps = 30
        self.running = 1
        self.type_display = "menu"
        # smallfont = pygame.font.SysFont('Corbel', 35)
        # self.text = smallfont.render('quit', True, (255, 255, 255))
        self.display = pygame.display.set_mode((self.display_w, self.display_h))

        self.colors = {
            "light": (187, 148, 87),
            "base1": (153, 88, 42),
            "base2": (111, 29, 27),
            "dark": (67, 40, 24)
        }

        self.init_menu()

        pygame.display.set_caption("Office Nightmare")
        self.clock = pygame.time.Clock()


    def button(self, coords, layout, texts, fonts, colors, funcs):
            self.btn_array = ButtonArray(
            self.display,  # Surface to place button array on
            coords[0], coords[1], coords[2] - coords[0], coords[3] - coords[1],
            layout,
            # border=100,  # Distance between buttons and edge of array
            texts=texts,
            fonts=fonts, #list(map(lambda el: el["name"], fonts)),
            colour=colors[0]["hover"],
            inactiveColours=list(map(lambda el: el["base"], colors)),  # Colour of button when not being interacted with
            hoverColours=list(map(lambda el: el["hover"], colors)),  # Colour of button when being hovered over
            pressedColours=list(map(lambda el: el["press"], colors)),  # Colour of button when being clicked
            textColours=list(map(lambda el: el["press"], colors)),
            onClicks=funcs
        )


    def label_text(self, coords, text, font, color):
        f = font
        res_label = f.render(text, True, color)
        self.display.blit(res_label, coords)
        pygame.display.update()


    def init_menu(self):
        self.display.fill(self.colors["dark"])
        self.menu = Menu(self, self.colors)
        self.button(coords=self.menu.buttons["coords"],
                    layout=self.menu.buttons["layout"],
                    texts=self.menu.buttons["texts"],
                    fonts=self.menu.buttons["fonts"],
                    colors=self.menu.buttons["colors"],
                    funcs=self.menu.buttons["funcs"])
        self.label_text(coords=self.menu.text_label_title["coords"],
                        text=self.menu.text_label_title["text"],
                        font=self.menu.text_label_title["font"],
                        color=self.menu.text_label_title["color"])


    def game_quit(self):
        self.running = 0

    def game_start(self):
        self.type_display = "game"

    def show_menu(self):
        while self.running:
            events = pygame.event.get()
            self.clock.tick(self.fps)

            for event in events:
                if event.type == pygame.QUIT: self.running = False
            pygame_widgets.update(events)
            pygame.display.update()

    def show_game(self):
        while self.running and self.type_display == "game":
            events = pygame.event.get()
            self.clock.tick(self.fps)

            self.display.fill(self.colors["dark"])

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            pygame_widgets.update(events)
            pygame.display.update()

if __name__ == "__main__":
    menu = Main()
    menu.show_menu()