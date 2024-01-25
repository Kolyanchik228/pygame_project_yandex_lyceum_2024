from player import Player
from settings import *
from ray_casting import ray_casting_walls
from drawing import Drawing
from interaction import Interaction


pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface(MINIMAP_RES)

clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map, player, clock)
interaction = Interaction(player, drawing)

drawing.menu()
pygame.mouse.set_visible(False)
interaction.play_music()
start_ticks = pygame.time.get_ticks()

while True:
    seconds=(pygame.time.get_ticks()-start_ticks) / 1000
    player.movement()
    drawing.background(player.angle)
    walls = ray_casting_walls(player, drawing.textures)
    drawing.world(walls)
    drawing.fps_and_clock(clock, seconds)
    drawing.mini_map(player)

    interaction.check_win(player.finish_collision)

    pygame.display.flip()
    clock.tick()
