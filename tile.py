from constants import WIDTH, HEIGHT, GRID_SIZE, TYPES
import pygame


class Tile:
    def __init__(self, type=None):
        self.rot = 0 # 90deg rotations of image(counterclockwise): 0, 1, 2, 3
        self.entropy = 5 # number of unique images, including rotations
        if type:
            self._type = type
            self._img = self.scale(TYPES[self._type]['img'])
            self._rect = self._img.get_rect()
            self._desc = TYPES[self._type]['description']
        else:
            self._type = None
            self._img = None
            self._rect = None
            self._desc = None

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, newType):
        self._type = newType
        self._img = self.scale(TYPES[self._type]['img'])
        self._rect = self._img.get_rect()
        self._desc = TYPES[self._type]['description']

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
        img.convert_alpha()
        return pygame.transform.scale(img, (WIDTH/GRID_SIZE, HEIGHT/GRID_SIZE))

    def rotate(self, count):
        '''
        Description:

            rotates tile image and updates related variables

        :count: int -> amount of 90deg rotations
        '''

        self.rot = count % 4
        self._img = pygame.transform.rotate(self._img, 90 * self.rot * -1)
        self._desc = self._desc[-self.rot:] + self._desc[:-self.rot]

