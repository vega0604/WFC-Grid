import os
import pygame

def loadImage(filename) -> pygame.Surface:
    '''
    Description:

        Loads and returns single image as pygame.Surface instance

    :filename: string -> file to loaded
    :returns: pygame.Surface -> pygame image surface
    '''

    filename = os.path.join(filename)
    return pygame.image.load(filename).convert_alpha()

def loadImages(amount) -> list:
    '''
    Description:

        Loads multiple images as pygame.Surface instances 
        and returns them all in a list

    :amount: int -> amount of files to load
    :returns: list -> list of pygame.Surface objects
    '''
    
    images = []
    for x in range(amount):
        images.append(loadImage(f'./resources/wfc{x}.png'))

    return images
