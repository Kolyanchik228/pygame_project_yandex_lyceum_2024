from settings import *
import pygame


class Interaction:
    def __init__(self, player, drawing):
        self.player = player
        self.drawing = drawing

    def play_music(self):
        THEME.play()

    def check_win(self, win):
        if win:
            THEME.stop()
            POBEDA.play()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                self.drawing.pobeda()
