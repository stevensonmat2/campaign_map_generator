from enum import Enum
from random import randint, random
from map import Map, Quadrant
from tile import Tile

class Type(Enum):
    mountain = 1
    forest = 2
    desert = 3
    grasslands = 4
    city = 5

tile_type_counts = {
    "mountain": 8,
    "forest": 6,
    "desert": 15,
    "grasslands": 28,
    "city": 15
}
center_quad_requirements = {
    "mountain_min": 3,
    "mountain_max": 4,
    "forest_min": 2,
    "forest_max": 3,
    "desert_min": 2,
    "desert_max": 3,
    "grasslands_min": 4,
    "grasslands_max": 5,
    "city_min": 1,
    "city_max":3
}

player_quadrants = {
    "desert_min": 1,
    "desert_max": 3,
    "grasslands_min": 4,
    "grasslands_max": 6,
    "city_min": 1,
    "city_max":3
}

PLAYER_QUADRANT_SIZE = 9
PLAYER_QUADRANT_COUNT = 2
CENTER_QUARDRANT_SIZE = 15
CENTER_QUARDRANT_COUNT = 2

pqc = 2
cqc = 2
map = Map()

tiles = []
exclusions = []

def randint_with_exclusion(start, end, exclusion_list: list):
    pick = None
    while(pick == None or exclusion_list.contains(pick)):
        pick = randint(start, end)

def generate_tiles():
    for key in 
for _ in range(1, 67):
    pick = randint_with_exclusion(1, 5, exclusions)
    type = Type(pick).name
    tile_type_counts[type] -= 1
    tiles.append(Tile(type))


while(pqc or cqc):
    if pqc:
        quad = Quadrant(PLAYER_QUADRANT_SIZE)
        # for _ in range(PLAYER_QUADRANT_SIZE):

