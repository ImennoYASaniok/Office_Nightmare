import pygame

class Menu():
    def __init__(self, parent, base_color):
        self.base_color = base_color
        self.parent = parent
        self.init_butons()
        self.init_label_text()

    def init_butons(self):
        self.general_param_buttons = {
            "color": {
                "base": self.base_color["base1"],
                "hover": self.base_color["base2"],
                "press": self.base_color["light"],
                "text": self.base_color["light"]
            },
            "font": pygame.font.SysFont("Century Gothic", 40)
        }
        self.button_start = {"text": "старт", "font":self.general_param_buttons["font"], "func": lambda: print("start"), "color":self.general_param_buttons["color"]} # self.parent.game_start
        self.button_sett = {"text": "настройки", "font":self.general_param_buttons["font"], "func":lambda: print("settings") , "color":self.general_param_buttons["color"]}
        self.button_quit = {"text": "выход", "font":self.general_param_buttons["font"], "func":self.parent.game_quit, "color":self.general_param_buttons["color"]}
        self.array_buttons = [self.button_start, self.button_sett, self.button_quit]

        self.buttons = {
            "coords":(200, 200, 500, 600),
            "layout":(1, 3),
            "size": 50
        }
        for key in self.array_buttons[0]: self.buttons[key+"s"] = list(map(lambda b: b[key], self.array_buttons))
        print(*list(map(lambda x: f"{x[0]}: ({len(x[1]) if type(x[1]) != int else None}) {x[1]}", self.buttons.items())), sep="\n")

    def init_label_text(self):
        self.general_param_text_label = {
            "color": {
                "base": self.base_color["light"],
                "dark": self.base_color["dark"],
            },

        }
        self.text_label_title = { "coords": (600, 200), "text":"Office Nightmare", "font": pygame.font.SysFont("Century Gothic", 80), "color":self.general_param_text_label["color"]["base"] }