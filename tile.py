from constants import WIDTH, HEIGHT, GRID_SIZE, TYPES, DEFAULT_ENTROPY
from loader import loadImage
from random import choice
from math import sqrt
import pygame


class Tile:
    def __init__(self, x=None, y=None, type=None):
        # Position Properties
        self.x = x
        self.y = y
        self.pos = (x, y)
        # Image Properties
        self.rot = 0 # 90deg rotations of image(counterclockwise): 0, 1, 2, 3
        self.possibilities = []

        if type != None:
            self.type = type
        else:
            self._type = None
            self._img = None
            self._rect = None
            self._desc = None

        # Logic Properties
        self.entropy = DEFAULT_ENTROPY # number of unique images, including rotations
        self.collapsed = False
        
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, newType):
        self._type = newType
        self._img = self.scale(loadImage(TYPES[self._type]['img']).convert_alpha())
        self._rect = self._img.get_rect()
        self._desc = TYPES[self._type]['description']
        self.collapsed = True

    @property
    def img(self):
        return self._img
    
    @property
    def desc(self):
        return self._desc
    
    @property
    def rect(self):
        return self._rect

    def scale(self, img):
        '''
        Description:

            returns scaled version of image

        :returns: pygame.Surface -> scaled image
        '''
        return pygame.transform.scale(img, (WIDTH/GRID_SIZE, HEIGHT/GRID_SIZE))

    def rotate(self, count):
        '''
        Description:

            rotates tile image and updates related variables

        :count: int -> amount of 90deg rotations
        '''
        count = count % 4
        self.rot += count
        self.rot = self.rot % 4
        self._img = pygame.transform.rotate(self._img, 90 * self.rot * -1)
        self._rect = self._img.get_rect()
        self._desc = self._desc[-count:] + self._desc[:-count]

    def collapse(self):
        chosen = choice(self.possibilities)
        self.type = chosen.type
        self.rotate(chosen.rot)

    def checkPossible(self, neighbour):
        
        for t in TYPES.keys():
            for r in range(4):
                tempTile = Tile(self.x, self.y, type=t)
                # print(tempTile.desc, neighbour.desc)
                tempTile.rotate(r)
                if neighbour.y < self.y:
                    if neighbour.desc[2] == tempTile.desc[0]:
                        self.possibilities.append(tempTile)
                elif neighbour.x > self.x:
                    if neighbour.desc[3] == tempTile.desc[1]:
                        self.possibilities.append(tempTile)
                elif neighbour.y > self.y:
                    if neighbour.desc[0] == tempTile.desc[2]:
                        self.possibilities.append(tempTile)
                elif neighbour.x < self.x:
                    if neighbour.desc[1] == tempTile.desc[3]:
                        self.possibilities.append(tempTile)

        return len(self.possibilities)
    

    def diff(self, tile):
        difference = (tile.x-self.x, tile.y-self.y)
        mag = sqrt((difference[0]**2 + difference[1]**2))
        return mag

    def calcEnt(self, grid):
        self.possibilities = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                neighbour = next((t for t in grid if t.pos == (self.x+x, self.y+y)), None)
                if not neighbour or not neighbour.collapsed or self.diff(neighbour) != 1:
                    continue
                # print(neighbour.pos, self.pos)

                self.entropy = self.checkPossible(neighbour)
                
        
