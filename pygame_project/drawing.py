from settings import *
from map import mini_map
import sys
import time


class Drawing:
    def __init__(self, sc, sc_map, player, clock):
        self.sc = sc
        self.sc_map = sc_map
        self.player = player
        self.clock = clock
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.font_win = pygame.font.Font('font/button_font.ttf', 144)
        self.textures = {1: WALL,
                         2: FINISH,
                         'S': SKY
                         }

        self.menu_trigger = True

        self.menu_picture = pygame.image.load('images/background.jpg').convert()

    def background(self, angle):
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, LAVANDER, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def fps_and_clock(self, clock, seconds):
        display_fps = str(int(clock.get_fps()))
        fps_render = self.font.render(display_fps, 0, DARKORANGE)
        self.sc.blit(fps_render, FPS_POS)
        time_render = self.font.render(str(seconds), 0, DARKORANGE)
        self.sc.blit(time_render, TIMER_POS)


    def mini_map(self, player):
        self.sc_map.fill(LAVANDER)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, LIGHT_STEEL_BLUE, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)

    def pobeda(self):
        render = self.font_win.render('ПОБЕДА!!!', 1, ROSY_BROWN)
        rect = pygame.Rect(0, 0, 1000, 300)
        rect.center = HALF_WIDTH, HALF_HEIGHT
        pygame.draw.rect(self.sc, LIGHT_STEEL_BLUE, rect, border_radius=50)
        self.sc.blit(render, (rect.centerx - 430, rect.centery - 70))
        pygame.display.flip()
        self.clock.tick(15)

    def menu(self):
        x = 0
        button_font = pygame.font.Font('font/button_font.ttf', 72)
        label_font = pygame.font.Font('font/label_font.otf', 300)
        start = button_font.render('СТАРТ', 1, ROSY_BROWN)
        button_start = pygame.Rect(0, 0, 400, 150)
        button_start.center = HALF_WIDTH, HALF_HEIGHT
        exit = button_font.render('ВЫХОД', 1, ROSY_BROWN)
        button_exit = pygame.Rect(0, 0, 400, 150)
        button_exit.center = HALF_WIDTH, HALF_HEIGHT + 200

        while self.menu_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.sc.blit(self.menu_picture, (0, 0), (x % WIDTH, 0, WIDTH, HEIGHT))
            x += 1

            pygame.draw.rect(self.sc, BLACK, button_start, border_radius=25, width=10)
            self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 40))

            pygame.draw.rect(self.sc, BLACK, button_exit, border_radius=25, width=10)
            self.sc.blit(exit, (button_exit.centerx - 140, button_exit.centery - 40))

            label = label_font.render('Find Cat', 1, ROSY_BROWN)
            self.sc.blit(label, (15, -30))

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if button_start.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, BLACK, button_start, border_radius=25)
                self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 40))
                if mouse_click[0]:
                    self.menu_trigger = False
            elif button_exit.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, BLACK, button_exit, border_radius=25)
                self.sc.blit(exit, (button_exit.centerx - 140, button_exit.centery - 40))
                if mouse_click[0]:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(20)
