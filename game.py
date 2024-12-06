import pygame, pygame_widgets

class Game():
    def __init__(self, parent, base_color):
        self.base_color = base_color
        self.parent = parent
        self.init_label_test()

    def init_label_test(self):
        # !!! Если нужно будет создавать много label -> сделай init_label_title общей для всех и возвращай label_title
        self.label_test = {
            "coords": (20, 20),
            "text": "здесь будет игра",
            "font": pygame.font.SysFont("Century Gothic", 40),
            "label": None
        }
        self.label_test["label"] = self.parent.label_text(coords=self.label_test["coords"],
                                                           text=self.label_test["text"],
                                                           font=self.label_test["font"])

    # def init_button_dop_menu(self):
    #     self.button_dop_menu = {
    #         "font": pygame.font.SysFont("Century Gothic", 40),
    #         "coords": (200, 200, 500, 600),
    #         "layout": (1, 3),
    #         "size": 50,
    #         "text": "...",
    #         "func": self.
    #     }
    #     self.buttons_general["buttons"] = self.parent.buttons(coords=self.buttons_general["coords"],
    #                                                           layout=self.buttons_general["layout"],
    #                                                           texts=self.buttons_general["texts"],
    #                                                           fonts=self.buttons_general["fonts"],
    #                                                           funcs=self.buttons_general["funcs"])

    def reinstall(self, _type):
        if _type == "hide":
            pass
        elif _type == "show":
            self.parent.display.blit(self.label_test["label"], self.label_test["coords"])
