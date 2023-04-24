from constants import DESCRIPTIONS


class Tile:
    def __init__(self, rot, type, img):
        self.rot = 0 # 90deg rotations of image(clockwise): 0, 1, 2, 3
        self.desc = DESCRIPTIONS[type] # list of strings describing tile side composition: "rr", "gg", "bb", etc.
        self.img = img # pygame.Surface object

    