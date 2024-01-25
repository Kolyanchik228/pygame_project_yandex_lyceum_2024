import math
import pygame
pygame.display.set_mode()

# игра
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PENTA_HEIGHT = 5 * HEIGHT
DOUBLE_HEIGHT = 2 * HEIGHT
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)
TIMER_POS = (65, 5)

# миникарта
MINIMAP_SCALE = 5
MINIMAP_RES = (WIDTH // MINIMAP_SCALE, HEIGHT // MINIMAP_SCALE)
MAP_SCALE = 2 * MINIMAP_SCALE
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MINIMAP_SCALE)

# ray casting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS



# текстуры
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
HALF_TEXTURE_HEIGHT = TEXTURE_HEIGHT // 2
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# игрок
player_pos = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
player_angle = 0
player_speed = 3
DOUBLE_PI = math.pi * 2

# цвета
BLACK = (0, 0, 0)
RED = (220, 0, 0)
YELLOW = (220, 220, 0)
DARKORANGE = (255, 140, 0)
LAVANDER_BLUSH = (255, 240, 245)
LAVANDER = (230, 230, 250)
ROSY_BROWN = (188, 143, 143)
LIGHT_STEEL_BLUE = (176, 196, 222)

# файлы
WALL = pygame.image.load('images/wall.png').convert()
FINISH = pygame.image.load('images/finish.png').convert()
SKY = pygame.image.load('images/sky.png').convert()
pygame.mixer.init()
THEME = pygame.mixer.Sound('sounds/theme.mp3')
POBEDA = pygame.mixer.Sound('sounds/pobeda.mp3')