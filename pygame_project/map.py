from settings import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int32

_ = False
map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 1, 1, _, 1, _, 1, 1, 1, 1, 1, _, 1, _, 1, 1, 1, _, 1, _, 1, _, 1],
    [1, _, _, 1, _, 1, _, 1, _, _, 1, 1, 1, 1, 1, 1, _, _, _, 1, _, 1, _, 1],
    [1, _, 1, 1, _, 1, _, 1, 1, _, _, _, 1, _, _, _, _, 1, _, 1, 1, 1, _, 1],
    [1, _, 1, 1, _, 1, _, _, _, _, 1, _, 1, _, 1, _, 1, 1, _, _, _, _, _, 1],
    [1, _, 1, 1, _, 1, 1, _, 1, 1, 1, _, 1, _, 1, _, _, 1, 1, _, _, 1, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 1, 1, _, _, 1, 1, _, 1],
    [1, _, 1, 1, 1, _, _, _, 1, _, 1, 1, 1, 1, 1, _, _, _, _, 1, 1, _, _, 1],
    [1, _, 1, _, _, _, 1, _, 1, 1, 1, _, _, _, 1, _, _, 1, _, _, _, _, 1, 1],
    [1, _, 1, _, 1, 1, 1, _, 1, _, 1, 1, 1, _, 1, 1, 1, 1, _, 1, 1, _, _, 1],
    [1, _, 1, 1, 1, _, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 1, 1, _, 1],
    [1, _, 1, _, _, _, 1, _, 1, _, 1, _, 1, 1, 1, 1, 1, _, 1, _, 1, 1, _, 1],
    [1, _, 1, 1, 1, _, 1, _, 1, _, 1, _, 1, _, _, _, 1, 1, 1, 1, 1, _, _, 1],
    [1, _, _, _, 1, _, _, _, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]
]

WORLD_WIDTH = len(map[0]) * TILE
WORLD_HEIGHT = len(map) * TILE
world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
mini_map = set()
collision_walls = []
for j, row in enumerate(map):
    for i, char in enumerate(row):
        if char:
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == 1:
                world_map[(i * TILE, j * TILE)] = 1
            elif char == 2:
                world_map[(i * TILE, j * TILE)] = 2
                finish = pygame.Rect(i * TILE, j * TILE, TILE, TILE)
